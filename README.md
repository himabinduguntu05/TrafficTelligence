# 🚦 Traffic Volume Prediction App

This is a machine learning-based web application built with **Flask** that predicts traffic volume based on various inputs like weather conditions, time features, and more.

## 🧠 Project Overview

This application uses a pre-trained machine learning model to predict traffic volume. The model is trained on traffic and weather data and considers the following features:

- Holiday
- Temperature
- Rain
- Snow
- Weather condition
- Year, Month, Day
- Hour, Minute, Second

The web app takes user input, preprocesses the data (using saved scaler and encoders), and returns the predicted traffic volume.

---

## 🚀 Tech Stack

- Python 3.8+
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML + CSS (for frontend)
- Pickle / Joblib (for model and scaler persistence)

---

## 📁 Project Structure



---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/himabinduguntu05/TrafficTelligence.git
cd your-repo-name/Flask


### 2.Install Dependencies

pip install -r requirements.txt
## 🚀 How to Run This Project

1. **Train the Model and Generate Required Files**

   Run the notebook `traffic_volume.ipynb` to train the model and generate the necessary `.pkl` files:

   - `traffic_volume_model.pkl`
   - `scaler.pkl`
   - `encoder.pkl` (if label encoding is used)

   These files are saved in the `Flask/` directory and are required for the Flask app to function.

2. **Run the Flask Web Application**

   After generating the `.pkl` files, run the Flask app:

   ```bash
   cd Flask
   python app.py



🌐 Usage
Fill in the input form (date, weather, temperature, etc.).

Click Predict.

The app will show the predicted traffic volume based on your input.