from flask import Flask
from flask import request
from flask import jsonify
import random

app = Flask(__name__)

@app.route("/predict")
def predict():
    days_tolerated = int(request.values['days'])
    max_temperature = int(request.values['temperature'])
    out = {"tolerated_days":days_tolerated, "max_tolerated_temperature":max_temperature, "prediction":"Some fancy stuff :D"}
    return jsonify(out)



@app.route("/demo")
def demo():
    days_tolerated = int(request.values['days'])
    max_temperature = int(request.values['temperature'])
    out = {"tolerated_days": 1, "max_tolerated_temperature": 2, "prediction": 0}
    bias = 0.7
    if random.random() > bias:
        out["prediction"] = 1
    return jsonify(out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)