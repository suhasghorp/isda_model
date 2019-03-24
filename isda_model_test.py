from isda.isda_model import *
from isda.cds_trade import *
from isda.market_data import *
import datetime


value_date = datetime.date(2019, 3, 21)
trade_date = datetime.date(2016, 5, 5)
effective_date = datetime.date(2016, 5, 6)
accrual_start_date = datetime.date(2016, 3, 20)
maturity_date = datetime.date(2019, 6, 20)

cds = CDSTrade(trade_date=trade_date,
               effective_date=effective_date,
               accrual_start_date=accrual_start_date,
               maturity_date=maturity_date,
               running_coupon=500.,
               recovery_rate=0.4,
               is_buy_protection=False,
               notional=10000000.)

market = Market_Data(value_date)
model = ISDAModel(cds, market)
valuation = model.single_name_pricer()
print('clean_pv:{0}'.format(valuation['clean_pv']))
print('dirty_pv:{0}'.format(valuation['dirty_pv']))
print('accrued_premium:{0}'.format(valuation['accrued_premium']))
print('days_accrued:{0}'.format(valuation['days_accrued']))
print('cs01:{0}'.format(valuation['cs01']))
print('dv01:{0}'.format(valuation['dv01']))