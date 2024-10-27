from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

app = Flask(__name__)

# Load the model and other necessary objects
reg = pickle.load(open('Prediction_model.pkl', 'rb'))
imputer = SimpleImputer(strategy='mean')  # Use mean imputation for missing values

@app.route('/predict_price', methods=['POST'])
def predict_price_route():
    data = request.json
    Area = data.get('Area')
    Type = data.get('Type')
    Bathrooms = data.get('Bathrooms')
    Furnished = data.get('Furnished')
    Level = data.get('Level')
    Payment_Option = data.get('Payment_Option')
    Delivery_Term = data.get('Delivery_Term')
    Bedrooms = data.get('Bedrooms')
    Price_range = data.get('Price_range')
    City = data.get('City')

    # Convert input to numpy array
    X = np.array([[Area, Level, Bedrooms,Type,Bathrooms,Furnished,Payment_Option,Delivery_Term,Price_range,City]])

    # Fit the imputer
    imputer.fit(X)

    # Handle missing values
    X_imputed = imputer.transform(X)

    # Make prediction
    prediction = reg.predict(X_imputed)[0]

    return jsonify({'Total_Price_EGP': prediction})
if __name__ == '__main__':
    app.run(debug=True)