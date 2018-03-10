from flask import Flask
from flask import request
from flask import jsonify
import random

from offTomorrow import off_tomorrow

app = Flask(__name__)

@app.route("/predict")
def predict():
    days_tolerated = int(request.values['days'])
    max_temperature = int(request.values['maxTemperature'])
    desired_temperature = int(request.values['desiredTemperature'])
    out = {"tolerated_days": days_tolerated,
           "max_tolerated_temperature": max_temperature,
           "desired_temperature": desired_temperature,
           "prediction": off_tomorrow(desired_temperature, max_temperature, days_tolerated)}
    return jsonify(out)



@app.route("/demo")
def demo():
    days_tolerated = int(request.values['days'])
    max_temperature = int(request.values['maxTemperature'])
    desired_temperature = int(request.values['desiredTemperature'])
    out = {"tolerated_days": days_tolerated, "max_tolerated_temperature": max_temperature, "desired_temperature": desired_temperature, "prediction": 0}
    bias = 0.7
    if random.random() > bias:
        out["prediction"] = 1
    return jsonify(out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)