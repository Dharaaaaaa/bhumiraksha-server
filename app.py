from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from models.predict import predict
from datetime import datetime

app = Flask(__name__)
CORS(app, support_credentials=False)
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# , methods=["POST"]
@app.route("/predict", methods=["POST"])
def predict_route():
    body = request.get_json()
    # Get the crop from the request
    crop = body['crop']
    try: 
      month = months[int(body['month'])-2]
      year = '2024'
      day = '25'
      start_date = year + '-' + month + '-' + day
      end_date = '2026' + '-' + month + '-' + day
    # Make predictions using the loaded model
      predictions = predict(crop, start_date, end_date)
    except:
      predictions = predict(crop)
    print(crop)
    print(type(predictions))
    # Return the predictions as JSON
    return jsonify({"predictions": predictions[-24:], "crop": crop})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)
