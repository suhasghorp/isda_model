from isda.isda_model import *
from isda.cds_trade import *
from isda.market_data import *
import datetime


# calypso id 751320
value_date = datetime.date(2019, 3, 25)
trade_date = datetime.date(2017, 5, 23)
effective_date = datetime.date(2017, 5, 24)
accrual_start_date = datetime.date(2019, 3, 20)
maturity_date = datetime.date(2022, 6, 20)

cds = CDSTrade(trade_date=trade_date,
               effective_date=effective_date,
               accrual_start_date=accrual_start_date,
               maturity_date=maturity_date,
               running_coupon=100.,
               recovery_rate=0.4,
               is_buy_protection=False,
               notional=10000000.)

market = Market_Data(value_date)
model = ISDAModel(cds, market)
valuation = model.single_name_pricer()
print('clean_price:{}'.format(valuation['clean_price']))
print('clean_pv:{}'.format(valuation['clean_pv']))
print('clean_pv:{}'.format(valuation['clean_pv']))
print('dirty_pv:{}'.format(valuation['dirty_pv']))
print('accrued_premium:{}'.format(valuation['accrued_premium']))
print('days_accrued:{}'.format(valuation['days_accrued']))
print('cs01:{}'.format(valuation['cs01']))
print('dv01:{}'.format(valuation['dv01']))

'''
===========  RESULTS =================

Date:b'20190325', Discount Factor:1.0, Survival Probability:1.0
Date:b'20191220', Discount Factor:0.979837848962938, Survival Probability:0.9991997384333375
Date:b'20200620', Discount Factor:0.9678563756969, Survival Probability:0.9985080697070057
Date:b'20210620', Discount Factor:0.9485677030262475, Survival Probability:0.9951798218094804
Date:b'20220620', Discount Factor:0.9286233994806836, Survival Probability:0.9888712188950224
Date:b'20230620', Discount Factor:0.9083608592263271, Survival Probability:0.9791645449036298
Date:b'20240620', Discount Factor:0.8877584529954312, Survival Probability:0.9640569735308748
Date:b'20290620', Discount Factor:0.7799060452407993, Survival Probability:0.8626710983061056
Date:b'20490620', Discount Factor:0.4516639049389472, Survival Probability:0.5807081639661118


Date:b'20190620', CashFlow:255555555.55555552
Date:b'20190920', CashFlow:255555555.55555552
Date:b'20191220', CashFlow:252777777.7777778
Date:b'20200320', CashFlow:252777777.7777778
Date:b'20200622', CashFlow:261111111.11111113
Date:b'20200921', CashFlow:252777777.7777778
Date:b'20201221', CashFlow:252777777.7777778
Date:b'20210322', CashFlow:252777777.7777778
Date:b'20210621', CashFlow:252777777.7777778
Date:b'20210920', CashFlow:252777777.7777778
Date:b'20211220', CashFlow:252777777.7777778
Date:b'20220321', CashFlow:252777777.7777778
Date:b'20220620', CashFlow:255555555.55555552


clean_price:0.025057756083701112

clean_pv:250577.56083701111

dirty_pv:252244.22750367783

accrued_premium:1666.6666666666913

days_accrued:0.000600000000000009

cs01:-3209.7197985990824

dv01:-39.82733796460691

'''