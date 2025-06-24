#importing all nexessary libraries
from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
import os
# Initialize Flask app
app = Flask(__name__)
model=pickle.load(open('/home/ghima/Desktop/Traffic_Telligence/Flask/traffic_volume_model.pkl', 'rb'))
# Load encoders and scaler
with open("/home/ghima/Desktop/Traffic_Telligence/Flask/encoder.pkl", "rb") as f:
    label_encoders = pickle.load(f)

with open("/home/ghima/Desktop/Traffic_Telligence/Flask/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

#rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
   
    raw_features = request.form.to_dict()
    
    # Convert to DataFrame
    df = pd.DataFrame([raw_features])
    
    # Apply label encoding
    # for col in label_encoders:
    #     le = label_encoders[col]
    #     df[col] = le.transform(df[col].astype(str))

    # Ensure correct order
    df = df[['holiday','temp','rain','snow','weather','day','month','year','hours','minutes','seconds']]
    
    # Scale
    df_scaled = scaler.transform(df)
    
    # Predict
    prediction = model.predict(df_scaled)[0]

    return render_template('result.html', prediction=int(prediction))
       

# Run the app
if __name__ == '__main__':
    port=int(os.environ.get('PORT', 5000))
    app.run(port=port,debug=True, use_reloader=False)  # Set use_reloader to False to avoid double execution