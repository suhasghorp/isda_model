from isda.c_interface import *

class CDSTrade:

    def __init__(self, **kwargs):

        self.arg_trade_date = kwargs['trade_date']
        self.arg_effective_date = kwargs['effective_date']
        self.arg_accrual_start_date = kwargs['accrual_start_date']
        self.arg_maturity_date = kwargs['maturity_date']
        self.is_buy_protection = kwargs['is_buy_protection']

        if self.is_buy_protection:
            self.credit_risk_direction_scale_factor = -1.0
        else:
            self.credit_risk_direction_scale_factor = 1.0

        self.c_interface = CInterface()

        self.trade_date = self.py_to_jpm_date(self.arg_trade_date)
        self.effective_date = self.py_to_jpm_date(self.arg_effective_date)
        self.accrual_start_date = self.py_to_jpm_date(self.arg_accrual_start_date)
        self.maturity_date = self.py_to_jpm_date(self.arg_maturity_date)

        badDayConvModified = ord('N')
        holidayNone = 'None'

        interval = TDateInterval()
        self.c_interface.JpmcdsStringToDateInterval('1D', 'CDSTrade', interval)
        start_date = (c_int * 1)()
        success = self.c_interface.JpmcdsDateFwdThenAdjust(self.trade_date, interval, badDayConvModified, holidayNone, start_date)


        self.running_coupon = kwargs['running_coupon']
        if 'par_spread' in kwargs:
            self.par_spread = kwargs['par_spread']
        self.recovery_rate = kwargs['recovery_rate']
        self.notional = kwargs['notional']

        self.refob = 'TARGET CORP' #calypso id 664070

        self.credit_spreads = [0.00064278,0.0007136,0.00127052,0.00202109,0.00288513,0.00401699,0.00803556, 0.00988759]

        self.single_basis_point = 0.0001

        self.credit_spreads_cs01 = [s + self.single_basis_point for s in self.credit_spreads]

        self.credit_spread_tenors = ['6M', '1Y', '2Y', '3Y', '4Y', '5Y', '10Y', '30Y']

        if len(self.credit_spreads) != len(self.credit_spread_tenors):
            raise ValueError('CDS Trade - credit spread tenors and spreads do not match')

        self.upfront_charge = None
        self.accrued_premium = None
        self.days_accrued = None
        self.clean_price = None
        self.dirty_price = None
        self.clean_pv = None
        self.dirty_pv = None
        self.cs01 = None
        self.dv01 = None

    def py_to_jpm_date(self,pydate):
        return self.c_interface.JpmcdsDate(pydate.year, pydate.month,pydate.day)
