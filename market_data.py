
class Market_Data:

    def __init__(self, valuation_date):

        self.valuation_date = valuation_date

        self.instr_names = 'MMMMMSSSSSSSSSSSSSS'

        self.expiries = ["1M", "2M", "3M", "6M", "1Y", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "8Y", "9Y", '10Y', '12Y', '15Y', '20Y', '25Y', '30Y']

        self.rates = [0.024906, 0.025444, 0.026070, 0.026790, 0.028135,
                      0.025040, 0.024225, 0.023880, 0.023910, 0.024125,
                      0.024310, 0.024615, 0.024975, 0.025350, 0.025925,
                      0.026505, 0.027040, 0.0272, 0.02726]

        if len(self.expiries) != len(self.rates):
            raise ValueError('Market Data tenors and rates do not match')
