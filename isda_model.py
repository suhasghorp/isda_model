from ctypes import *
from isda.c_interface import *
from isda.utils import *
from datetime import datetime


class ISDAModel:

    def __init__(self, cds, market):
        self.cds = cds
        self.market = market
        self.c_interface = CInterface()

    def buildZeroCurve(self, shift=None):

        valuation_date = self.py_to_jpm_date(self.market.valuation_date)
        routine = 'BuildExampleZeroCurve'
        badDayConvModified = ord('N')
        holidayNone = 'None'
        nInstr = len(self.market.instr_names)
        adv_dates = []
        for i in range(nInstr):
            tmp = TDateInterval()
            self.c_interface.JpmcdsStringToDateInterval(self.market.expiries[i], routine, tmp)
            dt = (c_int * 1)()
            success = self.c_interface.JpmcdsDateFwdThenAdjust(valuation_date, tmp, badDayConvModified, holidayNone, dt)
            adv_dates.append(dt[0])
        dates = (c_int * len(adv_dates))(*adv_dates)

        temp_rates = None
        if shift is None:
            temp_rates = self.market.rates
        else:
            temp_rates = [r + shift for r in self.market.rates]

        rates = (c_double * len(temp_rates))(*temp_rates)

        type = (c_long * 1)()
        self.c_interface.JpmcdsStringToDayCountConv('Act/360', type)
        mmDCC = c_long(type[0])

        tmp = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('6M', 'BuildExampleZeroCurve', tmp)
        freq_p = (c_double * 1)()
        self.c_interface.JpmcdsDateIntervalToFreq(tmp, freq_p)
        fixedSwapFreq = c_long(int(freq_p[0]))

        tmp = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('3M', 'BuildExampleZeroCurve', tmp)
        freq_p = (c_double * 1)()
        self.c_interface.JpmcdsDateIntervalToFreq(tmp, freq_p)
        floatSwapFreq = c_long(int(freq_p[0]))

        type = (c_long * 1)()
        self.c_interface.JpmcdsStringToDayCountConv('30/360', type)
        swapDCC = c_long(type[0])

        type = (c_long * 1)()
        self.c_interface.JpmcdsStringToDayCountConv('ACT/360', type)
        floatDCC = c_long(type[0])

        zero_curve = self.c_interface.JpmcdsBuildIRZeroCurve(
                        valuation_date,
                        self.market.instr_names,
                        dates,
                        rates,
                        nInstr,
                        fixedSwapFreq,
                        floatSwapFreq,
                        mmDCC,
                        swapDCC,
                        floatDCC,
                        badDayConvModified,
                        holidayNone)

        return zero_curve[0], adv_dates[-1]

    def ymd_to_jpm_date(self, ymd):
        dt = datetime.strptime(ymd,'%m/%d/%Y').date()
        return self.c_interface.JpmcdsDate(dt.year, dt.month,dt.day)

    def print_discount_factors(self, start_date, end_date, zero_curve):
        three_month_interval = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('3M', 'test', three_month_interval)
        date_list = self.c_interface.JpmcdsNewDateList(start_date, end_date,three_month_interval, 0)
        for i in range(date_list[0].fNumItems):
            dt = date_list[0].fArray[i]
            print('Date:{}, Disc factor:{}'.format(self.c_interface.JpmcdsFormatDate(dt),
                                                   self.c_interface.JpmcdsZeroPrice(zero_curve, dt)))

    def print_surv_probability(self, start_date,end_date, credit_curve):
        three_month_interval = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('3M', 'test', three_month_interval)
        date_list = self.c_interface.JpmcdsNewDateList(start_date, end_date, three_month_interval, 0)
        for i in range(date_list[0].fNumItems):
            dt = date_list[0].fArray[i]
            print('Date:{}, Survival Probability:{}'.format(self.c_interface.JpmcdsFormatDate(dt),
                                                            self.c_interface.JpmcdsZeroPrice(credit_curve, dt)))

    def buildCreditCurve(self, zero_curve, shift=None):

        valuation_date = self.py_to_jpm_date(self.market.valuation_date)
        future_imm_dates = Utils.imm_date_vector(datetime.combine(self.market.valuation_date, datetime.min.time()), tenor_list=[0.5, 1, 2, 3, 4, 5, 7, 10])
        jpm_imm_dates = [self.ymd_to_jpm_date(dt[1]) for dt in future_imm_dates]
        tenors = (c_int * len(jpm_imm_dates))(*jpm_imm_dates)

        nbDates = len(jpm_imm_dates)

        temp_spreads = None
        if shift is None:
            temp_spreads = self.cds.credit_spreads
        else:
            temp_spreads = [s + shift for s in self.cds.credit_spreads]

        spreads = (c_double * len(temp_spreads))(*temp_spreads)

        include = None  # include all dates and rates
        pay_accrual_on_default = True
        coupon_interval = None  # 3M is assumed

        type = (c_long * 1)()
        self.c_interface.JpmcdsStringToDayCountConv('Act/360', type)
        self.paymentDCC = type[0]

        self.stubFS = TStubMethod(False, False)
        ret = self.c_interface.JpmcdsStringToStubMethod('F/S', byref(self.stubFS))

        bad_day_conv_none = ord('N')
        bad_day_conv_modified = ord('M')
        bad_day_conv_following = ord('F')
        calendar = 'None'

        one_day_interval = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('1D', 'CDSTrade', one_day_interval)
        step_in_date = (c_int * 1)()
        success = self.c_interface.JpmcdsDateFwdThenAdjust(valuation_date, one_day_interval, bad_day_conv_none, calendar, step_in_date)

        three_days_interval = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('3D', 'CDSTrade', three_days_interval)
        cash_settle_date = (c_int * 1)()
        success = self.c_interface.JpmcdsDateFwdThenAdjust(valuation_date, three_days_interval, bad_day_conv_modified, calendar, cash_settle_date)

        self.c_interface.JpmcdsErrMsgOn
        self.c_interface.JpmcdsErrMsgEnableRecord(20,128)
        credit_curve = self.c_interface.JpmcdsCleanSpreadCurve(
            valuation_date,
            zero_curve,
            self.cds.effective_date,
            step_in_date[0],
            cash_settle_date[0],
            nbDates,
            tenors,
            spreads,
            include,
            self.cds.recovery_rate,
            pay_accrual_on_default,
            coupon_interval,
            self.paymentDCC,
            self.stubFS,
            bad_day_conv_following,
            calendar)

        return credit_curve[0],jpm_imm_dates[-1]

    def calc_cds_price(self, zero_curve, credit_curve, is_clean):

        valuation_date = self.py_to_jpm_date(self.market.valuation_date)

        bad_day_conv_none = ord('N')
        bad_day_conv_modified = ord('M')
        bad_day_conv_following = ord('F')
        calendar = 'None'

        one_day_interval = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('1D', 'CDSTrade', one_day_interval)
        step_in_date = (c_int * 1)()
        success = self.c_interface.JpmcdsDateFwdThenAdjust(valuation_date, one_day_interval, bad_day_conv_none,
                                                           calendar, step_in_date)

        three_days_interval = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('3D', 'CDSTrade', three_days_interval)
        cash_settle_date = (c_int * 1)()
        success = self.c_interface.JpmcdsDateFwdThenAdjust(valuation_date, three_days_interval, bad_day_conv_modified,
                                                           calendar, cash_settle_date)

        is_price_clean = is_clean
        cdsprice = (c_double * 1)()

        include = None  # include all dates and rates
        pay_accrual_on_default = True
        coupon_interval = None  # 3M is assumed

        ret = self.c_interface.JpmcdsCdsPrice(
            valuation_date,
            cash_settle_date[0],
            step_in_date[0],
            self.cds.accrual_start_date,
            self.cds.maturity_date,
            self.cds.running_coupon / 10000.,
            pay_accrual_on_default,
            coupon_interval,
            self.stubFS,
            self.paymentDCC,
            bad_day_conv_following,
            calendar,
            zero_curve,
            credit_curve,
            self.cds.recovery_rate,
            is_price_clean,
            cdsprice)

        return cdsprice[0] * -1.0

    def get_upfront_charge(self, running_coupon):

        isPriceClean = False
        cdsprice = (c_double * 1)()

        self.coupon_interval = TDateInterval()
        self.JpmcdsStringToDateInterval('3M', 'BuildExampleZeroCurve', self.coupon_interval)

        ret = self.JpmcdsCdsPrice(
            self.cds.today,
            self.cds.cash_settle_date,
            self.cds.step_in_date,
            self.cds.start_date,
            self.cds.maturity_date,
            self.cds.running_coupon/10000.,
            self.payAccrualOnDefault,
            byref(self.couponInterval),
            self.stubFS,
            self.paymentDCC,
            self.badDayConvFollowing,
            self.calendar,
            self.zeroCurve[0],
            self.creditCurve[0],
            self.cds.recovery_rate,
            isPriceClean,
            cdsprice)

        self.cds.upfront_charge = cdsprice[0] * self.cds.notional
        print('Upfront Charge: %s' % self.upfrontCharge)

    def get_accrued_premium(self):

        c = CInterface()
        isPriceClean = True
        cdsprice = (c_double * 1)()

        ret = self.c_interface.JpmcdsCdsPrice(
            self.cds.today,
            self.cds.cash_settle_date,
            self.cds.step_in_date,
            self.cds.start_date,
            self.cds.maturity_date,
            self.cds.running_coupon/10000.,
            self.payAccrualOnDefault,
            byref(self.coupon_interval),
            self.stubFS,
            self.paymentDCC,
            self.badDayConvFollowing,
            self.calendar,
            self.zeroCurve[0],
            self.creditCurve[0],
            self.cds.recovery_rate,
            isPriceClean,
            cdsprice)

        self.cds.accrued_premium = cdsprice[0] * self.cds.notional - self.cds.upfront_charge
        print('Accrued Premium: %s' % self.cds.accrued_premium)
        self.cds.days_accrued = self.cds.accrued_premium * (360. / self.cds.running_coupon) / self.cds.notional
        print('Days Accrued: %s' % self.cds.days_accrued)
        self.cds.clean_price = (self.cds.notional - self.cds.upfront_charge - self.cds.accrued_premium) / self.cds.notional * 100.
        print('Clean Price: %s' % self.cds.clean_price)

    def py_to_jpm_date(self,pydate):
        return self.c_interface.JpmcdsDate(pydate.year, pydate.month,pydate.day)

    def single_name_pricer(self):

        zero_curve, last_date = self.buildZeroCurve(shift=None)
        self.print_discount_factors(self.py_to_jpm_date(self.market.valuation_date), last_date, zero_curve)
        credit_curve, last_date = self.buildCreditCurve(zero_curve, shift=None)
        self.print_surv_probability(self.py_to_jpm_date(self.market.valuation_date), last_date, credit_curve)
        clean_price = self.calc_cds_price(zero_curve, credit_curve, is_clean=True)
        dirty_price = self.calc_cds_price(zero_curve, credit_curve, is_clean=False)
        clean_pv = clean_price * self.cds.notional * self.cds.credit_risk_direction_scale_factor
        dirty_pv = dirty_price * self.cds.notional * self.cds.credit_risk_direction_scale_factor
        accrued_premium = (dirty_price - clean_price) * self.cds.notional
        days_accrued = accrued_premium * (360. / self.cds.running_coupon) / self.cds.notional

        zero_curve_shifted, last_date = self.buildZeroCurve(shift=0.0001)
        credit_curve_shifted, last_date = self.buildCreditCurve(zero_curve_shifted, shift=0.0001)

        dirty_price_shifted_cs01 = self.calc_cds_price(zero_curve, credit_curve_shifted, is_clean=False)
        cs01 = (dirty_price_shifted_cs01 - dirty_price) * self.cds.notional * self.cds.credit_risk_direction_scale_factor

        dirty_price_shifted_dv01 = self.calc_cds_price(zero_curve_shifted, credit_curve, is_clean=False)
        dv01 = (dirty_price_shifted_dv01 - dirty_price) * self.cds.notional * self.cds.credit_risk_direction_scale_factor

        return {'clean_pv' : clean_pv, 'dirty_pv' : dirty_pv, 'accrued_premium' : accrued_premium, 'days_accrued' : days_accrued, 'cs01' : cs01, 'dv01' : dv01}
