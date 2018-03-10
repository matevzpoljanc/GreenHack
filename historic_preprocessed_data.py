from datetime import date

weather_data = dict()

with open("daily_data.txt","r") as f:
    for line in f.readlines():
        time, value = line.strip().split()
        weather_data[time] = float(value)

def data_for_past_year(year, month, day):
    d0 = date(int(year), int(month), int(day))

    data_last_year = dict()

    for key, value in weather_data.items():
        d1 = date(*list(map(int, [key[:4], key[5:7], key[8:10]])))
        # print(d0,d1,(d1-d0).days)
        if (d1-d0).days in range(-365,1):
            data_last_year[key] = value

    return data_last_year

print(len(weather_data))
# for key, value in data_for_past_year(2013,2,3).items():
#     print(key,value)

