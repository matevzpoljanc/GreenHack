from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/predict")
def predict():
    days_tolerated = int(request.values['days'])
    max_temperature = int(request.values['temperature'])
    out = {"tolerated_days":days_tolerated, "max_tolerated_temperature":max_temperature, "prediction":"Some fancy stuff :D"}
    return jsonify(out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)