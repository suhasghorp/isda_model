import calendar
import datetime

class Utils:

    @staticmethod
    def add_month(date):
        month_days = calendar.monthrange(date.year, date.month)[1]
        candidate = date + datetime.timedelta(days=month_days)
        return candidate.replace(day=1) - datetime.timedelta(days=1) \
            if candidate.day != date.day \
            else candidate

    @staticmethod
    def remove_month(date):
        candidate = date.replace(day=1) - datetime.timedelta(days=1)
        return candidate.replace(day=date.day)

    @staticmethod
    def move_n_months(date, i, n, direction='add'):
        if i == n:
            return date
        else:
            i += 1
            return Utils.move_n_months(Utils.add_month(date) if direction == 'add'
                                           else Utils.remove_month(date), i, n, direction)
    @staticmethod
    def next_imm(s_date,
                 semi_annual_roll_start=datetime.datetime(2015, 12, 20),
                 imm_month_list=[3, 6, 9, 12], imm_semi_annual_roll_months=[3, 9]):

        imm_date_count = 0
        imm_day_of_month = 20
        months_between_imm_dates = 3
        one_day = datetime.timedelta(1)

        # break after reaching first immdate
        while True:
            if imm_date_count >= 1:
                break
            s_date = s_date + one_day
            if s_date.day == imm_day_of_month \
                    and s_date.month in imm_month_list:
                imm_date_count += 1

        # semi annual roll date adjustment, implemented after 2015
        if s_date >= semi_annual_roll_start:
            # move back 3 months to previous imm date
            if s_date.month in imm_semi_annual_roll_months:
                s_date = Utils.move_n_months(s_date, 0,
                                       months_between_imm_dates,
                                       direction='remove')

        # adjust day for day of week? Modified Following
        return datetime.datetime(s_date.year, s_date.month, imm_day_of_month)

    def imm_date_vector(start_date,tenor_list, format='%m/%d/%Y'):

        tenors = [float(x[:-1])/12 if x[-1] == 'M' else float(x[:-1]) for x in tenor_list]
        # need a better date add that knows which month?
        return [(x, Utils.next_imm(Utils.move_n_months(start_date, 0, (6 if x == 0.5 else x * 12)))) for x in
                tenors] if format == '' \
            else [('{0}{1}'.format((6 if x == 0.5 else x), ('Y' if x >= 1 else 'M')),
                   Utils.next_imm(Utils.move_n_months(start_date, 0, (6 if x == 0.5 else x * 12))).strftime(format)) for x in
                  tenors]