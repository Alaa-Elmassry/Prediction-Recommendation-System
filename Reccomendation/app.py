# import pandas as pd
# from sklearn.neighbors import NearestNeighbors
# import pickle

# # Example data: Replace with your actual data
# data_encoded_refernce = pd.DataFrame({
#     'bedrooms': [2, 3, 4, 3, 5],
#     'area': [1000, 1500, 2000, 1800, 2500],
#     'price': [200000, 250000, 300000, 280000, 350000],
#     'Bathrooms': [1, 2, 2, 3, 2],
#     'Level': [1, 2, 3, 4, 5]
# })

# # Train the NearestNeighbors model with the new features
# model = NearestNeighbors(metric='cosine')
# model.fit(data_encoded_refernce[['bedrooms', 'area', 'price', 'Bathrooms', 'Level']])

# # Save the model

# with open('recommendation_model4.pkl', 'wb') as model_file:
#     pickle.dump(model, model_file)
# ****************************************************************
import os
from pathlib import Path

# الحصول على المسار المطلق
relative_path = './Egyption.csv'
absolute_path = Path(relative_path).resolve()

print(f"Checking existence of: {absolute_path}")

if absolute_path.exists():
    print(f"The file {absolute_path} exists.")
else:
    print(f"The file {absolute_path} does not exist.")




