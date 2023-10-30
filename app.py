# Import necessary libraries and modules
import pickle
from flask import Flask, request
from flask_cors import CORS, cross_origin
import pandas as pd

# Declare the Flask app
app = Flask(__name__)

# Enable cross-origin request support
cors = CORS(app)

# Load the machine learning model from a pickle file
model = pickle.load(open("./Output/model.pkl", "rb"))

# Define an API route for status check
@app.route('/check', methods=['GET'])
@cross_origin()
def return_status():
    return "Yay! Flask App is running"

# Define an API route for getting time series predictions
@app.route('/', methods=['POST'])
@cross_origin()
def return_model_prediction():
    try:
        # Get the last residual variance from the model
        predictions = model.residual_variance.tail(1).values[0]
        final_predictions = list(predictions)
        return {"status_code": 200, "message": "Success", "body": {"preds": final_predictions}}

    except Exception as e:
        print(f"Error occurred: {e}")
        return {"status_code": 404, "message": f"Error: {e}"}

if __name__ == '__main__':
    # Run the Flask app on 0.0.0.0 and port 5000
    app.run("0.0.0.0", port=5000)
