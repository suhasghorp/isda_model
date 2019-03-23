from ctypes import *

class CInterface:

    def __init__(self):
        self.dll = CDLL('ISDA_Clib.dll')

    #define the prototypes of various functions exported by dll

    #C signature
    #int JpmcdsDateIntervalToFreq (TDateInterval *interval, double *freq); '''

    def JpmcdsErrMsgOn(self):
        func = self.dll.JpmcdsErrMsgOn
        return func()

    def JpmcdsErrMsgEnableRecord(self, lines, length):
        func = self.dll.JpmcdsErrMsgEnableRecord
        func.argtypes = [c_int, c_int]
        func.restype = c_int
        return func(lines,length)

    def JpmcdsDateIntervalToFreq(self, interval, freq):
      func = self.dll.JpmcdsDateIntervalToFreq
      func.argtypes = [POINTER(TDateInterval), POINTER(c_double)]
      func.restype = c_int
      return func(byref(interval), freq)


    #C signature
    #int JpmcdsStringToDayCountConv(char *dayCountString, long *type);

    def JpmcdsStringToDayCountConv(self, dayCountString, type):
      func = self.dll.JpmcdsStringToDayCountConv
      func.argtypes = [POINTER(c_char), POINTER(c_long)]
      func.restype = c_int
      return func(dayCountString.encode('utf-8'), type)

    #C signature
    #int  JpmcdsDateFwdThenAdjust
    #(TDate           date,               /* (I) Start date */
    # TDateInterval  *interval,           /* (I) Interval to advance by */
    # long            badDayMethod,       /* (I) JPMCDS_BAD_DAY_XYZ */
    # char           *holidayFile,        /* (I) Holiday file to use */
    # TDate          *advAdjustedDate);   /* (O) Advanced adjusted date */

    def JpmcdsDateFwdThenAdjust(self, date, interval, badDayMethod, holidayFile, advAdjustedDate):
      func = self.dll.JpmcdsDateFwdThenAdjust
      func.argtypes = [c_int, POINTER(TDateInterval), c_long, POINTER(c_char), POINTER(c_int)]
      func.restype = c_int
      return func(date, byref(interval), badDayMethod, holidayFile.encode('utf-8'), advAdjustedDate)

    #C signature
    '''int JpmcdsStringToDateInterval
        (char          *input,      /* (I) String w/ 1A, 3M, 4D, etc */
         char          *label,      /* (I) Label-for JpmcdsErr Msg only */
         TDateInterval *interval);  /* (O) Value read from file */'''

    def JpmcdsStringToDateInterval(self, input, label, interval):
        func = self.dll.JpmcdsStringToDateInterval
        func.argtypes = [POINTER(c_char), POINTER(c_char), POINTER(TDateInterval)]
        func.restype = c_int
        return func(input.encode('utf-8'), label.encode('utf-8'), byref(interval))

    #C signature
    #TDate JpmcdsDate
    #    (long year,  /* (I) Year */
    #    long month, /* (I) Month */
    #    long day    /* (I) Day */
    #    )

    def JpmcdsDate(self, year, month, day):
      func = self.dll.JpmcdsDate
      func.argtypes = [c_long, c_long, c_long]
      func.restype = c_int
      return func(year, month, day)

    #C signature
    '''TCurve* JpmcdsBuildIRZeroCurve(
        TDate      valueDate,      /* (I) Value date                       */
        char      *instrNames,     /* (I) Array of 'M' or 'S'              */
        TDate     *dates,          /* (I) Array of swaps dates             */
        double    *rates,          /* (I) Array of swap rates              */
        long       nInstr,         /* (I) Number of benchmark instruments  */
        long       mmDCC,          /* (I) DCC of MM instruments            */
        long       fixedSwapFreq,  /* (I) Fixed leg freqency               */
        long       floatSwapFreq,  /* (I) Floating leg freqency            */
        long       fixedSwapDCC,   /* (I) DCC of fixed leg                 */
        long       floatSwapDCC,   /* (I) DCC of floating leg              */
        long       badDayConv,     /* (I) Bad day convention               */
        char      *holidayFile);   /* (I) Holiday file                     */'''

    def JpmcdsBuildIRZeroCurve(self, spotDate, instrNames, dates, rates, nInstr, swapFreq, floatFreq, mmDCC, swapDCC, floatDCC, badDayConv, holidayFile):
      func = self.dll.JpmcdsBuildIRZeroCurve
      func.argtypes = [c_int, POINTER(c_char), POINTER(c_int), POINTER(c_double), c_long, c_long, c_long, c_long, c_long, c_long, c_long, POINTER(c_char)]
      func.restype = POINTER(TCurve)
      return func(spotDate,instrNames.encode('utf-8'),dates,rates,nInstr,mmDCC,swapFreq,floatFreq,swapDCC,floatDCC,badDayConv,holidayFile.encode('utf-8'))

    #C signature
    '''TContingentLeg* JpmcdsCdsContingentLegMake(
        /** Date when protection begins. Either at start or end of day (depends
            on protectStart) */
        TDate     startDate,
        /** Date when protection ends (end of day) */
        TDate     endDate,
        /** Notional value protected */
        double    notional,
        /** Should protection include the start date */
        TBoolean  protectStart)'''

    def JpmcdsCdsContingentLegMake(self, startDate, endDate, notional, protectStart):
      func = self.dll.JpmcdsCdsContingentLegMake
      func.argtypes = [c_int, c_int, c_double, c_int]
      func.restype = POINTER(TContingentLeg)
      return func(startDate, endDate, notional, protectStart)

    #C signature
    '''int JpmcdsCdsContingentLegPV(
        /** Risk starts at the end of today */
        TDate             today,
        /** Date for which the PV is calculated and cash settled */
        TDate             valueDate,
        /** Date when protection begins. Either at start or end of day (depends
            on protectStart) */
        TDate             startDate,
        /** Date when protection ends (end of day) */
        TDate             endDate,
        /** Notional value protected */
        double            notional, 
        /** Interest rate discount curve - assumes flat forward interpolation */
        TCurve           *discCurve,
        /** Credit clean spread curve */
        TCurve           *spreadCurve,
        /** Assumed recovery rate in case of default */
        double            recoveryRate,
        /** True => protection includes start date */
        TBoolean          protectStart,
        /** Output - the present value is returned */
        double           *pv)'''

    def JpmcdsCdsContingentLegPV(self, today, valueDate, startDate, endDate, notional, discCurve, spreadCurve, recoveryRate, protectStart, pv):
      func = self.dll.JpmcdsCdsContingentLegPV
      func.argtypes = [c_int, c_int, c_int, c_int, c_double, POINTER(TCurve), POINTER(TCurve), c_double, c_int, POINTER(c_double)]
      func.restype = c_int
      return func(today, valueDate, startDate, endDate, notional, discCurve, spreadCurve, recoveryRate, protectStart, pv)

    #C signature
    '''TFeeLeg* JpmcdsCdsFeeLegMake(
        /** Date when protection begins. Either at start or end of day (depends
            on protectStart) */
        TDate           startDate,
        /** Date when protection ends (end of day) */
        TDate           endDate,
        /** Should accrued interest be paid on default. Usually set to TRUE */
        TBoolean        payAccOnDefault,
        /** Interval between coupon payments. Can be NULL when 3M is assumed */
        TDateInterval  *couponInterval,
        /** If the startDate and endDate are not on cycle, then this parameter
            determines location of coupon dates. */
        TStubMethod    *stubType,
        /** Notional value protected */
        double          notional, 
        /** Fixed coupon rate (a.k.a. spread) for the fee leg */
        double          couponRate,
        /** Day count convention for coupon payment. Normal is ACT_360 */
        long            paymentDcc,
        /** Bad day convention for adjusting coupon payment dates. */
        long            badDayConv,
        /** Calendar used when adjusting coupon dates. Can be NULL which equals
            a calendar with no holidays and including weekends. */
        char           *calendar,
        /** Should protection include the start date */
        TBoolean        protectStart)'''

    def JpmcdsCdsFeeLegMake(self, startDate, endDate, payAccOnDefault, couponInterval, stubType, notional, couponRate, paymentDcc, badDayConv, calendar, protectStart):
      func = self.dll.JpmcdsCdsFeeLegMake
      func.argtypes = [c_int, c_int, c_int, POINTER(TDateInterval), POINTER(TStubMethod), c_double, c_double, c_long, c_long, POINTER(c_char), c_int]
      func.restype = POINTER(TFeeLeg)
      return func(startDate, endDate, payAccOnDefault, couponInterval, byref(stubType), notional, couponRate, paymentDcc, badDayConv, calendar, protectStart)  #byref(couponInterval), calendar.encode('utf-8')

    #C signature
    '''int JpmcdsCdsFeeLegPV(
        /** Risk starts at the end of today */
        TDate           today,
        /** Date for which the PV is calculated and cash settled */
        TDate           valueDate,
        /** Date when step-in becomes effective */
        TDate           stepinDate,
        /** Date when protection begins. Either at start or end of day (depends
            on protectStart) */
        TDate           startDate,
        /** Date when protection ends (end of day) */
        TDate           endDate,
        /** Should accrued interest be paid on default. Usually set to TRUE */
        TBoolean        payAccOnDefault,
        /** Interval between coupon payments. Can be NULL when 3M is assumed */
        TDateInterval  *couponInterval,
        /** If the startDate and endDate are not on cycle, then this parameter
            determines location of coupon dates. */
        TStubMethod    *stubType,
        /** Notional value protected */
        double          notional, 
        /** Fixed coupon rate (a.k.a. spread) for the fee leg */
        double          couponRate,
        /** Day count convention for coupon payment. Normal is ACT_360 */
        long            paymentDcc,
        /** Bad day convention for adjusting coupon payment dates. */
        long            badDayConv,
        /** Calendar used when adjusting coupon dates. Can be NULL which equals
            a calendar with no holidays and including weekends. */
        char           *calendar,
        /** Interest rate discount curve - assumes flat forward interpolation */
        TCurve         *discCurve,
        /** Credit clean spread curve */
        TCurve         *spreadCurve,
        /** Should protection include the start date */
        TBoolean        protectStart,
        /** Should the present value be computed as a clean price (removing
            accrued interest) */
        TBoolean        isPriceClean,
        /** Output - the present value is returned */
        double         *pv)'''

    def JpmcdsCdsFeeLegPV(self, today, valueDate, stepinDate, startDate, endDate, payAccOnDefault, couponInterval, stubType, notional, couponRate, paymentDcc, badDayConv, calendar, discCurve, spreadCurve, protectStart, isPriceClean, pv):
      func = self.dll.JpmcdsCdsFeeLegPV
      func.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, POINTER(TDateInterval), POINTER(TStubMethod), c_double, c_double, c_long, c_long, POINTER(c_char), POINTER(TCurve), POINTER(TCurve), c_int, c_int, POINTER(c_double)]
      func.restype = c_int
      return func(today, valueDate, stepinDate, startDate, endDate, payAccOnDefault, couponInterval, stubType, notional, couponRate, paymentDcc, badDayConv, calendar.encode('utf-8'), discCurve, spreadCurve, protectStart, isPriceClean, pv)#byref(couponInterval), calendar.encode('utf-8')

    #C signature
    '''int JpmcdsCdsPrice(
        /** Risk starts at the end of today */
        TDate           today,
        /** Date for which the PV is calculated and cash settled */
        TDate           valueDate,
        /** Date when step-in becomes effective */
        TDate           stepinDate,
        /** Date when protection begins. Either at start or end of day (depends
            on protectStart) */
        TDate           startDate,
        /** Date when protection ends (end of day) */
        TDate           endDate,
        /** Fixed coupon rate (a.k.a. spread) for the fee leg */
        double          couponRate,
        /** Should accrued interest be paid on default. Usually set to TRUE */
        TBoolean        payAccOnDefault,
        /** Interval between coupon payments. Can be NULL when 3M is assumed */
        TDateInterval  *couponInterval,
        /** If the startDate and endDate are not on cycle, then this parameter
            determines location of coupon dates. */
        TStubMethod    *stubType,
        /** Day count convention for coupon payment. Normal is ACT_360 */
        long            paymentDcc,
        /** Bad day convention for adjusting coupon payment dates. */
        long            badDayConv,
        /** Calendar used when adjusting coupon dates. Can be NULL which equals
            a calendar with no holidays and including weekends. */
        char           *calendar,
        /** Interest rate discount curve - assumes flat forward interpolation */
        TCurve         *discCurve,
        /** Credit clean spread curve */
        TCurve         *spreadCurve,
        /** Assumed recovery rate in case of default */
        double          recoveryRate,
        /** Is the price expressed as a clean price (removing accrued interest) */
        TBoolean        isPriceClean,
        /** Output - price (a.k.a. upfront charge) for the CDS is returned 
            (see also isPriceClean) */
        double         *price)'''

    def JpmcdsCdsPrice(self, today, valueDate, stepinDate, startDate, endDate, couponRate, payAccOnDefault, couponInterval, stubType, paymentDcc, badDayConv, calendar, discCurve, spreadCurve, recoveryRate, isPriceClean, price):
      func = self.dll.JpmcdsCdsPrice
      func.argtypes = [c_int, c_int, c_int, c_int, c_int, c_double, c_int, POINTER(TDateInterval), POINTER(TStubMethod), c_long, c_long, POINTER(c_char), POINTER(TCurve), POINTER(TCurve), c_double, c_int, POINTER(c_double)]
      func.restype = c_int
      return func(today, valueDate, stepinDate, startDate, endDate, couponRate, payAccOnDefault, couponInterval, stubType, paymentDcc, badDayConv, calendar.encode('utf-8'), discCurve, spreadCurve, recoveryRate, isPriceClean, price)

    #C signature
    '''int JpmcdsCdsParSpreads(
        /** Risk starts at the end of today */
        TDate           today,
        /** Date when step-in becomes effective  */
        TDate           stepinDate,
        /** Date when protection begins. Either at start or end of day (depends
            on protectStart) */
        TDate           startDate,
        /** Number of benchmark dates */
        long            nbEndDates,
        /** Date when protection ends (end of day), no bad day adjustment */
        TDate          *endDates,
        /** Should accrued interest be paid on default. Usually set to TRUE */
        TBoolean        payAccOnDefault,
        /** Interval between coupon payments. Can be NULL when 3M is assumed */
        TDateInterval  *couponInterval,
        /** If the startDate and endDate are not on cycle, then this parameter
            determines location of coupon dates. */
        TStubMethod    *stubType,
        /** Day count convention for coupon payment. Normal is ACT_360 */
        long            paymentDcc,
        /** Bad day convention for adjusting coupon payment dates. */
        long            badDayConv,
        /** Calendar used when adjusting coupon dates. Can be NULL which equals
            a calendar with no holidays and including weekends. */
        char           *calendar,
        /** Interest rate discount curve - assumes flat forward interpolation */
        TCurve         *discCurve,
        /** Credit clean spread curve */
        TCurve         *spreadCurve,
        /** Assumed recovery rate in case of default */
        double          recoveryRate,
        /** Output - par spreads for the CDS are returned (see also isPriceClean) */
        double         *parSpread)'''

    def JpmcdsCdsParSpreads(self, today, stepinDate, startDate, nbEndDates, endDate, payAccOnDefault, couponInterval, stubType, paymentDcc, badDayConv, calendar, discCurve, spreadCurve, recoveryRate, parSpread):
      func = self.dll.JpmcdsCdsParSpreads
      func.argtypes = [c_int, c_int, c_int, c_long, POINTER(c_int), c_int, POINTER(TDateInterval), POINTER(TStubMethod), c_long, c_long, POINTER(c_char), POINTER(TCurve), POINTER(TCurve), c_double, POINTER(c_double)]
      func.restype = c_int
      return func(today, stepinDate, startDate, nbEndDates, endDate, payAccOnDefault, couponInterval, stubType, paymentDcc, badDayConv, calendar.encode('utf-8'), discCurve, spreadCurve, recoveryRate, parSpread)

    #C signature
    '''TCashFlowList* JpmcdsCdsFeeLegFlows(
        /** Date when protection begins. Either at start or end of day (depends
            on protectStart) */
        TDate           startDate,
        /** Date when protection ends for each benchmark (end of day).*/
        TDate           endDate,
        /** Interval between coupon payments. Can be NULL when 3M is assumed */
        TDateInterval  *dateInterval,
        /** If the startDate and endDate are not on cycle, then this parameter
            determines location of coupon dates. */
        TStubMethod    *stubType,
        /** Notional of the fee leg */
        double          notional,
        /** Fixed coupon rate (a.k.a. spread) for the fee leg */
        double          couponRate,
        /** Day count convention for coupon payment. Normal is ACT_360 */
        long            paymentDcc,
        /** Bad day convention for adjusting coupon payment dates. */
        long            badDayConv,
        /** Calendar used when adjusting coupon dates. Can be NULL which equals
            a calendar with no holidays and including weekends. */
        char           *calendar)'''

    def JpmcdsCdsFeeLegFlows(self, startDate, endDate, dateInterval, stubType, notional, couponRate, paymentDcc, badDayConv, calendar):
      func = self.dll.JpmcdsCdsFeeLegFlows
      func.argtypes = [c_int, c_int, POINTER(TDateInterval), POINTER(TStubMethod), c_double, c_double, c_long, c_long, POINTER(c_char)]
      func.restype = POINTER(TCashFlowList)
      return func(startDate, endDate, dateInterval, stubType, notional, couponRate, paymentDcc, badDayConv, calendar.encode('utf-8'))

    #C signature
    '''TCurve* JpmcdsCleanSpreadCurve(
        /** Risk starts at the end of today */
        TDate           today,
        /** Interest rate discount curve - assumes flat forward interpolation */
        TCurve         *discCurve,
        /** Effective date of the benchmark CDS */
        TDate           startDate,
        /** Step in date of the benchmark CDS */
        TDate           stepinDate,
        /** Date when payment should be make */
        TDate           cashSettleDate,
        /** Number of benchmark dates */
        long            nbDate,
        /** Dates when protection ends for each benchmark (end of day).
            Array of size nbDate */
        TDate          *endDates,
        /** Coupon rates for each benchmark instrument. Array of size nbDate */
        double         *couponRates,
        /** Flags to denote that we include particular benchmarks. This makes it
            easy for the user to include or exclude benchmarks on a one-by-one
            basis. Can be NULL if all are included. Otherwise an array of size
            nbDate. */
        TBoolean       *includes,
        /** Recovery rate in case of default */
        double          recoveryRate,
        /** Should accrued interest be paid on default. Usually set to TRUE */
        TBoolean        payAccOnDefault,
        /** Interval between coupon payments. Can be NULL when 3M is assumed */
        TDateInterval  *couponInterval,
        /** Day count convention for coupon payment. Normal is ACT_360 */
        long            paymentDcc,
        /** If the startDate and endDate are not on cycle, then this parameter
            determines location of coupon dates. */
        TStubMethod    *stubType,
        /** Bad day convention for adjusting coupon payment dates. */
        long            badDayConv,
        /** Calendar used when adjusting coupon dates. Can be NULL which equals
            a calendar with no holidays and including weekends. */
        char           *calendar)'''

    def JpmcdsCleanSpreadCurve(self, today, discCurve, startDate, stepinDate, cashSettleDate, nbDate, endDates, couponRates, includes, recoveryRate, payAccOnDefault, couponInterval, paymentDcc, stubType, badDayConv, calendar):
      func = self.dll.JpmcdsCleanSpreadCurve
      func.argtypes = [c_int, POINTER(TCurve), c_int, c_int, c_int, c_long, POINTER(c_int), POINTER(c_double), POINTER(c_int), c_double, c_int, POINTER(TDateInterval), c_long, POINTER(TStubMethod), c_long, POINTER(c_char)]
      #func.argtypes = [c_int, POINTER(TCurve), c_int, c_int, c_int, c_long, POINTER(c_int), POINTER(c_double), POINTER(c_int), c_double, c_int, POINTER(TDateInterval), c_long, TStubMethod, c_long, POINTER(c_char)]
      func.restype = POINTER(TCurve)
      return func(today, discCurve, startDate, stepinDate, cashSettleDate, nbDate, endDates, couponRates, includes, recoveryRate, payAccOnDefault, couponInterval, paymentDcc, stubType, badDayConv, calendar.encode('utf-8'))

    #C signature
    '''int JpmcdsHolidayLoadFromDisk
    (char  *name,                        /* (I) name associated with holidays */
     char  *filename);                   /* (I) filename to load */'''

    def JpmcdsHolidayLoadFromDisk(self, name, file):
        func = self.dll.JpmcdsHolidayLoadFromDisk
        func.argtypes = [POINTER(c_char), POINTER(c_char)]
        func.restype = c_int
        return func(name.encode('utf-8'), file.encode('utf-8'))

    #C signature
    '''int JpmcdsStringToStubMethod
    (char        *name,      /* (I) Stub method name */
     TStubMethod *stubMethod /* (O) Stub method returned */
    )'''

    def JpmcdsStringToStubMethod(self, name, stubmethod):
        func = self.dll.JpmcdsStringToStubMethod
        #func.argtypes = [POINTER(c_char), POINTER(TStubMethod)]
        func.argtypes = [c_char_p, POINTER(TStubMethod)]
        func.restype = c_int
        return func(name.encode('utf-8'), stubmethod)

    #C signature
    '''double JpmcdsZeroPrice
    (TCurve* zeroCurve,
     TDate   date);'''

    def JpmcdsZeroPrice(self, creditCurve, date):
      func = self.dll.JpmcdsZeroPrice
      func.argtypes = [POINTER(TCurve), c_int]
      func.restype = c_float
      return func(creditCurve,date)

    #C signature
    #char* JpmcdsFormatDate(TDate date);

    def JpmcdsFormatDate(self, tdate):
      func = self.dll.JpmcdsFormatDate
      func.argtypes = [c_int]
      func.restype = c_char_p
      return func(tdate)

    #C signature
    '''int JpmcdsCdsoneUpfrontCharge
    (TDate           today,
     TDate           valueDate,
     TDate           benchmarkStartDate,  /* start date of benchmark CDS for
                                          ** internal clean spread bootstrapping */
     TDate           stepinDate,
     TDate           startDate,           /* CDS start date, can be in the past */
     TDate           endDate,
     double          couponRate,
     TBoolean        payAccruedOnDefault,
     TDateInterval  *dateInterval,
     TStubMethod    *stubType,
     long            accrueDCC,
     long            badDayConv,
     char           *calendar,
     TCurve         *discCurve,
     double          oneSpread,
     double          recoveryRate,
     TBoolean        payAccruedAtStart,
     double         *upfrontCharge)'''

    def JpmcdsCdsoneUpfrontCharge(self, today, settlementDate, startDate1, stepinDate, startDate2, maturityDate, coupon,
     payAccruedOnDefault, couponInterval, stub, accrueDCC, badDayConv, calendar, discCurve, oneSpread, recoveryRate,
     payAccruedAtStart, upfrontCharge) :
      func = self.dll.JpmcdsCdsoneUpfrontCharge
      func.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_int, POINTER(TDateInterval),POINTER(TStubMethod),
                       c_long, c_long, POINTER(c_char), POINTER(TCurve), c_double, c_double, c_int, POINTER(c_double)]
      func.restype = c_int
      return func(today, settlementDate, startDate1, stepinDate, startDate2, maturityDate, coupon,
        payAccruedOnDefault, couponInterval, stub, accrueDCC, badDayConv, calendar.encode('utf-8'), discCurve, oneSpread, recoveryRate,
        payAccruedAtStart, upfrontCharge)


class TRatePt(Structure):
    _fields_ = [
        ('fDate', c_int),
        ('fRate', c_double)
    ]


class TCurve(Structure):
    _fields_ = [
        ('fNumItems', c_int),
        ('fArray', POINTER(TRatePt)),
        ('fBaseDate', c_int),
        ('fBasis', c_double),
        ('fDayCountConv', c_long),
    ]

    def __init__(self, count):
        items = (TRatePt * count)()
        self.fArray = cast(items, POINTER(TRatePt))
        self.fNumItems = count
        for i in range(0, count):
            self.fArray[i].fDate = i
            self.fArray[i].fRate = i * .25


class TDateInterval(Structure):
    _fields_ = [
        ('prd', c_int),
        ('prd_type', c_char),
        ('flag', c_int)
    ]


class TStubMethod(Structure):
    _fields_ = [
        ('stubAtEnd', c_int),
        ('longStub', c_int)
    ]


class TCashFlow(Structure):
    _fields_ = [
        ('fDate', c_int),
        ('fAmount', c_double)
    ]


class TCashFlowList(Structure):
    _fields_ = [
        ('fNumItems', c_int),
        ('fArray', POINTER(TCashFlow))
    ]

    def __init__(self, count):
        items = (TCashFlow * count)()
        self.fArray = cast(items, POINTER(TCashFlow))
        self.fNumItems = count
        for i in range(0, count):
            self.fArray[i].fDate = i
            self.fArray[i].fAmount = i * .25


class TContingentLeg(Structure):
    _fields_ = [
        ('startDate', c_int),
        ('endDate', c_int),
        ('notional', c_double),
        ('payType', c_int),
        ('protectStart', c_int)
    ]


class TFeeLeg(Structure):
    _fields_ = [
        ('nbDates', c_int),
        ('accStartDates', POINTER(c_int)),
        ('accEnDates', POINTER(c_int)),
        ('payDates', POINTER(c_int)),
        ('notional', c_double),
        ('couponRate', c_double),
        ('dcc', c_long),
        ('accrualPayConv', c_int),
        ('obsStartOfDay', c_int)
    ]

