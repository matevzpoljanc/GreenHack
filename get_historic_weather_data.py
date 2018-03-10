import os
import numpy as np

from datetime import date

weather_data = dict()

for file in os.listdir("./daily-text"):
    with open("./daily-text/" + file, "r") as f:
        data = f.read()
        filered_data = []

        for line in data.split("\n"):
            if len(line) > 0 and line[0] == "#":
                continue

            l = line.split()

            if not len(l) > 0:
                continue
            try:
                time, temp = int(l[0].split(":")[0]), float(l[1])
            except:
                continue

            if time in range(6,21):
                filered_data.append(temp)

        if len(filered_data) > 0:
            weather_data[file] = np.mean(filered_data)

with open("daily_data.txt","w") as f:
    for key, value in weather_data.items():
        f.write(key + " " + str(round(value,1)) + "\n")

def data_for_past_year(year, month, day):
    d0 = date(int(year), int(month), int(day))

    data_last_year = dict()

    for key, value in weather_data.items():
        d1 = date(*list(map(int, [key[:4], key[5:7], key[8:10]])))
        # print(d0,d1,(d1-d0).days)
        if (d1-d0).days in range(-365,1):
            data_last_year[key] = value

    return data_last_year

# print(len(weather_data))
for key, value in data_for_past_year(2013,2,3).items():
    print(key,value)

