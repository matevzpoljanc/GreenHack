import requests

def getWeekPrediction():
    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20item.forecast%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22acton%2C%20ca%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
    rjson = r.json()
    predict_data_list = rjson["query"]["results"]["channel"]
    predict_data_temps = []
    for item in predict_data_list:
        temp = item["item"]["forecast"]["high"]
        # They're in Fahrenheit so turn to celsius
        temp_celsius = (5/9)*(int(temp)-32)
        predict_data_temps.append(temp_celsius)
    return predict_data_temps
