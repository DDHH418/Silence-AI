from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    area = data["area"]
    time = data["time"]
    traffic = int(data["traffic"])

    risk = "Low"

    if area == "residential":
        if time == "night" and traffic > 3:
            risk = "High"
        elif traffic > 5:
            risk = "Medium"

    if area == "industrial":
        if traffic > 7:
            risk = "Medium"
        if traffic > 9:
            risk = "High"

    return jsonify({"risk": risk})

if __name__ == "__main__":
    app.run(debug=True)
