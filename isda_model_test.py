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

''' =============  RESULTS ===============
Date:b'20190321', Disc factor:1.0
Date:b'20190621', Disc factor:0.9933817595903559
Date:b'20190921', Disc factor:0.986492289905093
Date:b'20191221', Disc factor:0.9793157988017906
Date:b'20200321', Disc factor:0.9721915149230991
Date:b'20200621', Disc factor:0.966940106606409
Date:b'20200921', Disc factor:0.9617170643975126
Date:b'20201221', Disc factor:0.9565785494893033
Date:b'20210321', Disc factor:0.9515235068122933
Date:b'20210621', Disc factor:0.9461635586764631
Date:b'20210921', Disc factor:0.9408338032198604
Date:b'20211221', Disc factor:0.9355915153693678
Date:b'20220321', Disc factor:0.930435565763677
Date:b'20220621', Disc factor:0.9251348553891761
Date:b'20220921', Disc factor:0.9198643432696734
Date:b'20221221', Disc factor:0.9146806583668087
Date:b'20230321', Disc factor:0.9095826693537203
Date:b'20230621', Disc factor:0.9041361730079943
Date:b'20230921', Disc factor:0.8987222897753404
Date:b'20231221', Disc factor:0.8933991449847752
Date:b'20240321', Disc factor:0.8881075292558386
Date:b'20240621', Disc factor:0.8825021898404405
Date:b'20240921', Disc factor:0.8769322288324162
Date:b'20241221', Disc factor:0.8714573956810983
Date:b'20250321', Disc factor:0.8660763452440469
Date:b'20250621', Disc factor:0.8605588486417167
Date:b'20250921', Disc factor:0.8550765022532492
Date:b'20251221', Disc factor:0.8496881062767554
Date:b'20260321', Disc factor:0.8443923223594356
Date:b'20260621', Disc factor:0.8387092388977839
Date:b'20260921', Disc factor:0.8330644047626322
Date:b'20261221', Disc factor:0.8275183031383728
Date:b'20270321', Disc factor:0.822069465188765
Date:b'20270621', Disc factor:0.8163018726940815
Date:b'20270921', Disc factor:0.8105747452994818
Date:b'20271221', Disc factor:0.8049493987408628
Date:b'20280321', Disc factor:0.7993630917946768
Date:b'20280621', Disc factor:0.7935436164357531
Date:b'20280921', Disc factor:0.7877665076731868
Date:b'20281221', Disc factor:0.7820935695796909
Date:b'20290321', Disc factor:0.7765231540950908
Date:b'20290621', Disc factor:0.7708493000803288
Date:b'20290921', Disc factor:0.7652169034505928
Date:b'20291221', Disc factor:0.7596862154981873
Date:b'20300321', Disc factor:0.7542556225321152
Date:b'20300621', Disc factor:0.7487444716160202
Date:b'20300921', Disc factor:0.7432735892554555
Date:b'20301221', Disc factor:0.7379014989802668
Date:b'20310321', Disc factor:0.732626633373565
Date:b'20310621', Disc factor:0.7272678742131348
Date:b'20310921', Disc factor:0.7219483114160788
Date:b'20311221', Disc factor:0.7167248485355469
Date:b'20320321', Disc factor:0.7115391786161352
Date:b'20320621', Disc factor:0.706334662539704
Date:b'20320921', Disc factor:0.7011682146236833
Date:b'20321221', Disc factor:0.6960951005458741
Date:b'20330321', Disc factor:0.6911138382719999
Date:b'20330621', Disc factor:0.6860587222783497
Date:b'20330921', Disc factor:0.6810405816660247
Date:b'20331221', Disc factor:0.6761130956643044
Date:b'20340321', Disc factor:0.6712748247819728
Date:b'20340621', Disc factor:0.6663943008680346
Date:b'20340921', Disc factor:0.6615492609508072
Date:b'20341221', Disc factor:0.6567915391785537
Date:b'20350321', Disc factor:0.6521197555331064
Date:b'20350621', Disc factor:0.6473784991294201
Date:b'20350921', Disc factor:0.6426717141737996
Date:b'20351221', Disc factor:0.6380497557083914
Date:b'20360321', Disc factor:0.6334610373865665
Date:b'20360621', Disc factor:0.6288554397574332
Date:b'20360921', Disc factor:0.6242833272651428
Date:b'20361221', Disc factor:0.6197936141727034
Date:b'20370321', Disc factor:0.6153849982001737
Date:b'20370621', Disc factor:0.6109108229605913
Date:b'20370921', Disc factor:0.6064691773473941
Date:b'20371221', Disc factor:0.602107579837453
Date:b'20380321', Disc factor:0.5978247653118536
Date:b'20380621', Disc factor:0.5934782622765334
Date:b'20380921', Disc factor:0.5891633606229764
Date:b'20381221', Disc factor:0.584926222871176
Date:b'20390321', Disc factor:0.5807656200028429
Date:b'20390621', Disc factor:0.5766966964320109
Date:b'20390921', Disc factor:0.5726562802976646
Date:b'20391221', Disc factor:0.5686876302811331
Date:b'20400321', Disc factor:0.5647464839932702
Date:b'20400621', Disc factor:0.5607897926859342
Date:b'20400921', Disc factor:0.5568608225004559
Date:b'20401221', Disc factor:0.5530016389230513
Date:b'20410321', Disc factor:0.5492111704860163
Date:b'20410621', Disc factor:0.5453633217153825
Date:b'20410921', Disc factor:0.5415424315008693
Date:b'20411221', Disc factor:0.5377894081713918
Date:b'20420321', Disc factor:0.534103209733688
Date:b'20420621', Disc factor:0.5303612094077528
Date:b'20420921', Disc factor:0.5266454260492204
Date:b'20421221', Disc factor:0.5229956426613388
Date:b'20430321', Disc factor:0.519410845914488
Date:b'20430621', Disc factor:0.5157717823041512
Date:b'20430921', Disc factor:0.5121582144724726
Date:b'20431221', Disc factor:0.5086088310530216
Date:b'20440321', Disc factor:0.5050840457407612
Date:b'20440621', Disc factor:0.5015927033264581
Date:b'20440921', Disc factor:0.49812549446370286
Date:b'20441221', Disc factor:0.49471955063003253
Date:b'20450321', Disc factor:0.4913739410742921
Date:b'20450621', Disc factor:0.48797736837273364
Date:b'20450921', Disc factor:0.4846042741366627
Date:b'20451221', Disc factor:0.4812907819391922
Date:b'20460321', Disc factor:0.4780359862936683
Date:b'20460621', Disc factor:0.47473161085638355
Date:b'20460921', Disc factor:0.47145007658031596
Date:b'20461221', Disc factor:0.46822652649292074
Date:b'20470321', Disc factor:0.4650600796862582
Date:b'20470621', Disc factor:0.4618453988918448
Date:b'20470921', Disc factor:0.45865293925349576
Date:b'20471221', Disc factor:0.45551688986913896
Date:b'20480321', Disc factor:0.45240228329022264
Date:b'20480621', Disc factor:0.44927509823399525
Date:b'20480921', Disc factor:0.4461695295283857
Date:b'20481221', Disc factor:0.44311883572781136
Date:b'20490321', Disc factor:0.44012218316121826


Date:b'20190321', Survival Probability:1.0
Date:b'20190620', Survival Probability:0.9984958380258422
Date:b'20190920', Survival Probability:0.9969774467204064
Date:b'20191220', Survival Probability:0.9954778311559567
Date:b'20200320', Survival Probability:0.9914815304706825
Date:b'20200620', Survival Probability:0.9874576225345796
Date:b'20200920', Survival Probability:0.9799854830599197
Date:b'20201220', Survival Probability:0.9726501875195381
Date:b'20210320', Survival Probability:0.9654495048529815
Date:b'20210620', Survival Probability:0.9581439018667125
Date:b'20210920', Survival Probability:0.9463725168551766
Date:b'20211220', Survival Probability:0.9348713573419507
Date:b'20220320', Survival Probability:0.9236340671432252
Date:b'20220620', Survival Probability:0.9122866565998493
Date:b'20220920', Survival Probability:0.8993347311207679
Date:b'20221220', Survival Probability:0.8867044907876092
Date:b'20230320', Survival Probability:0.8743875190556505
Date:b'20230620', Survival Probability:0.8619736556008712
Date:b'20230920', Survival Probability:0.8461179454379928
Date:b'20231220', Survival Probability:0.8307215214182523
Date:b'20240320', Survival Probability:0.8156052591346784
Date:b'20240620', Survival Probability:0.8006024797433011
Date:b'20240920', Survival Probability:0.7838969776189743
Date:b'20241220', Survival Probability:0.7677160000654518
Date:b'20250320', Survival Probability:0.7520413781609773
Date:b'20250620', Survival Probability:0.7363491599149408
Date:b'20250920', Survival Probability:0.7209843780582202
Date:b'20251220', Survival Probability:0.7061020244187972
Date:b'20260320', Survival Probability:0.6916853882436946
Date:b'20260620', Survival Probability:0.6772525679426935
Date:b'20260920', Survival Probability:0.6651408676192255
Date:b'20261220', Survival Probability:0.6533739119053686
Date:b'20270320', Survival Probability:0.6419410262530824
Date:b'20270620', Survival Probability:0.6304608227022339
Date:b'20270920', Survival Probability:0.6191859262873669
Date:b'20271220', Survival Probability:0.608231955891072
Date:b'20280320', Survival Probability:0.5974717713389781
Date:b'20280620', Survival Probability:0.5867868372557136
Date:b'20280920', Survival Probability:0.5762929880434677
Date:b'20281220', Survival Probability:0.5660978333046137
Date:b'20290320', Survival Probability:0.5561921243709577
Date:b'20290620', Survival Probability:0.546245418147137


clean_pv:116487.49186714189
dirty_pv:119265.26964491967
accrued_premium:2777.7777777777783
days_accrued:0.0002
cs01:-253.2332561137017
dv01:-2.974701802781893
'''