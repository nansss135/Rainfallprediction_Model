import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("🌧 Rainfall Prediction System")

# Inputs
day = st.number_input("Day", value=1)
pressure = st.number_input("Pressure", value=1020.0)
maxtemp = st.number_input("Max Temperature", value=25.0)
temperature = st.number_input("Temperature", value=22.0)
mintemp = st.number_input("Min Temperature", value=20.0)
dewpoint = st.number_input("Dew Point", value=18.0)
humidity = st.number_input("Humidity", value=80)
cloud = st.number_input("Cloud", value=70)
sunshine = st.number_input("Sunshine", value=5.0)
winddirection = st.number_input("Wind Direction", value=100.0)
windspeed = st.number_input("Wind Speed", value=15.0)

# Prediction
if st.button("Predict Rainfall"):

    input_data = np.array([[
        day,
        pressure,
        maxtemp,
        temperature,
        mintemp,
        dewpoint,
        humidity,
        cloud,
        sunshine,
        winddirection,
        windspeed
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("🌧 Rainfall Expected")
    else:
        st.success("☀ No Rainfall Expected")