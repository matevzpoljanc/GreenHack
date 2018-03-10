import csv
from datetime import date

weather_data = dict()

with open("1242686.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        weather_data[row['DATE']] = row['TMAX']

print(weather_data.keys())

def data_for_past_year(year, month, day):
    d0 = date(int(year), int(month), int(day))

    data_last_year = [[],[]]

    for key, value in weather_data.items():
        d1 = date(*list(map(int, [key[:4], key[5:7], key[8:10]])))
        # print(d0,d1,(d1-d0).days)
        if (d1-d0).days in range(-365,1):
            data_last_year[0].append(key)
            data_last_year[1].append(float(value))

    return data_last_year


