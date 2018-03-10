from costFunction import find_days, calc_gain
from california_data import data_for_past_year
from weekPredict import getWeekPrediction
from datetime import datetime

def off_tomorrow(t_in, t_highest, days_allowed):
    now = datetime.now()

    week_predict = getWeekPrediction()
    historical = data_for_past_year(now.year, now.month, now.day)[1]
    total_set = historical + week_predict
    todays_index = len(historical)

    hot_days = find_days(total_set, t_in, t_highest, days_allowed)
    if todays_index in hot_days:
        off_tomorrow = 1
    else:
        off_tomorrow = 0

    return off_tomorrow