# ************************************************************************************
from flask import Flask, request, jsonify
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

# تحميل نموذج التوصيات المدرب
model = pickle.load(open('recommendation_model4.pkl', 'rb'))

def get_data_from_csv():
    file_path = 'G:\AI_Prediction_Recommendation\Final_Prediction&Recommendation\Reccomendation\Egyption.csv'
    
    # التحقق من وجود الملف
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # تحميل البيانات من ملف CSV
    df = pd.read_csv(file_path)
    return df

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json

    # استخراج المدخلات من JSON
    bedrooms = data.get('bedrooms')
    area = data.get('area')
    price = data.get('price')
    bathrooms = data.get('bathrooms')
    level = data.get('level')

    if not (isinstance(bedrooms, list) and isinstance(area, list) and isinstance(price, list)
            and isinstance(bathrooms, list) and isinstance(level, list)):
        return jsonify({'error': 'All input features must be lists.'}), 400

    if len(bedrooms) != len(area) or len(area) != len(price) or len(price) != len(bathrooms) or len(bathrooms) != len(level):
        return jsonify({'error': 'All input lists must have the same length.'}), 400

    input_features = np.array(list(zip(bedrooms, area, price, bathrooms, level)))
    recommendations_list = []

    try:
        # تحميل البيانات من ملف CSV
        df = get_data_from_csv()
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 404

    # طباعة البيانات من ملف CSV للتحقق
    print("Data from CSV:", df.head())

    for features in input_features:
        print("Input features for recommendation:", features)
        recommendations = model.kneighbors([features], n_neighbors=5)[1]
        recommendations_list.append(recommendations.tolist())

    return jsonify({'recommendations': recommendations_list})

if __name__ == '__main__':
    app.run(debug=True)

