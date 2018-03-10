import numpy as np
# need to import the energy calculation

def find_days(year_data, t_in, t_highest, days_allowed):
    savings_list = []
    hot_streak = 0 
    hot_lull = 0 
    days_left = days_allowed
    for t_out in year_data:
        energy_saved = energy_calc(t_in, t_out) - energy_calc(t_highest, t_out)
        savings_list += [energy_saved]
    gain_list = savings_list
    hot_days = []
    for (i,day_saving) in enumerate(savings_list):
        gain = calc_gain(hot_streak, hot_lull, days_left, days_allowed, day_saving)
        gain_list[i] = gain
        if i in sorted(range(len(gain_list)), key=lambda i: gain_list[i])[-days_allowed:] and days_left > 0:
            hot_streak += 1
            hot_lull = 0
            days_left -= 1
            hot_days += [i]
        else:
            hot_streak = 0
            hot_lull += 1
    return hot_days

def energy_calc(t_in, t_out):
    energy = ((t_out-t_in)**2)/(273+t_out) # Needs to be in Kelvin on the bottom
    return energy

def calc_gain(hot_streak, hot_lull, days_left, days_allowed, e_saving):
    gain = e_saving
    gain = gain * np.exp(-hot_streak/days_allowed) * np.exp(hot_lull/365)
    return gain
