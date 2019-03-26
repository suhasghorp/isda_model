
class Market_Data:

    def __init__(self, valuation_date):

        self.valuation_date = valuation_date

        self.instr_names = 'MMMMMSSSSSSSSSSSSSS'

        self.expiries = ["1M", "2M", "3M", "6M", "1Y", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "8Y", "9Y", '10Y', '12Y', '15Y', '20Y', '25Y', '30Y']

        self.rates = [0.024989, 0.02556, 0.026099,0.026760,0.02787,0.024085,0.023125,0.022870,0.02282,0.023085,0.02327,0.023645,0.02392,0.024235,0.02491,0.02551,0.025985,0.02621,0.026205]

        if len(self.expiries) != len(self.rates):
            raise ValueError('Market Data tenors and rates do not match')

