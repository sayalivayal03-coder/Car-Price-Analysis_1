import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load model columns
model_columns = pickle.load(open("model_columns.pkl", "rb"))

# Title
st.title("🚗 Car Price Prediction App")

st.write("Enter car details below:")

# Inputs
year = st.number_input("Year", 1990, 2026, 2020)

engine_size = st.number_input("Engine Size", 0.5, 10.0, 2.0)

horsepower = st.number_input("Horsepower", 50, 1000, 150)

mpg_city = st.number_input("MPG City", 5, 100, 20)

mpg_highway = st.number_input("MPG Highway", 5, 100, 30)

weight = st.number_input("Weight", 500, 5000, 2500)

wheelbase = st.number_input("Wheelbase", 50, 150, 100)

length = st.number_input("Length", 100, 250, 180)

# Predict button
if st.button("Predict Price"):

    # Create empty dataframe
    input_data = pd.DataFrame(columns=model_columns)

    # Fill all columns with 0
    input_data.loc[0] = 0

    # Add user values
    if "Year" in model_columns:
        input_data["Year"] = year

    if "EngineSize" in model_columns:
        input_data["EngineSize"] = engine_size

    if "Horsepower" in model_columns:
        input_data["Horsepower"] = horsepower

    if "MPG_City" in model_columns:
        input_data["MPG_City"] = mpg_city

    if "MPG_Highway" in model_columns:
        input_data["MPG_Highway"] = mpg_highway

    if "Weight" in model_columns:
        input_data["Weight"] = weight

    if "Wheelbase" in model_columns:
        input_data["Wheelbase"] = wheelbase

    if "Length" in model_columns:
        input_data["Length"] = length

    # Prediction
    prediction = model.predict(input_data)

    # Output
    st.success(f"Estimated Car Price: ${prediction[0]:,.2f}")