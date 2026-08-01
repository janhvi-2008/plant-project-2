import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("plant_growth_model.pkl", "rb"))

st.title("🌿 Plant Growth Prediction")

st.write("Enter plant growth details below.")

days = st.number_input("Days", min_value=1, value=30)

temperature = st.number_input("Temperature (°C)", value=28.0)

humidity = st.number_input("Humidity (%)", value=65.0)

rainfall = st.number_input("Rainfall (mm)", value=100.0)

soil = st.number_input("Soil Moisture (%)", value=55.0)

sunlight = st.number_input("Sunlight (hours)", value=8.0)

fertilizer = st.number_input("Fertilizer (g)", value=20.0)

if st.button("Predict Plant Height"):

    data = np.array([[days,
                      temperature,
                      humidity,
                      rainfall,
                      soil,
                      sunlight,
                      fertilizer]])

    prediction = model.predict(data)

    st.success(f"Predicted Plant Height: {prediction[0]:.2f} cm")