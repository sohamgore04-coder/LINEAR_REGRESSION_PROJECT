import streamlit as st
import numpy as np
import pandas as pd
import pickle

# =========================
# Load Model & Files
# =========================
model = pickle.load(open("model.pkl", "rb"))

# If you used scaler
try:
    scaler = pickle.load(open("scaler.pkl", "rb"))
except:
    scaler = None

# If you saved training columns
try:
    columns = pickle.load(open("columns.pkl", "rb"))
except:
    columns = None


# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Medical Insurance Cost Predictor",
    page_icon="💰",
    layout="centered"
)

# =========================
# Title
# =========================
st.title("💰 Medical Insurance Cost Predictor")
st.markdown("Predict insurance charges based on user details")

st.divider()

# =========================
# User Inputs
# =========================
age = st.slider("Age", 18, 100, 25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.slider("Number of Children", 0, 5, 0)

sex = st.selectbox("Gender", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southeast", "southwest"])

# =========================
# Encode Input
# =========================
input_dict = {
    "age": age,
    "bmi": bmi,
    "children": children,
    "sex_male": 1 if sex == "male" else 0,
    "smoker_yes": 1 if smoker == "yes" else 0,
    "region_northwest": 1 if region == "northwest" else 0,
    "region_southeast": 1 if region == "southeast" else 0,
    "region_southwest": 1 if region == "southwest" else 0,
}

input_df = pd.DataFrame([input_dict])

# Align columns with training
if columns is not None:
    input_df = input_df.reindex(columns=columns, fill_value=0)

# Apply scaling if used
if scaler is not None:
    input_df = scaler.transform(input_df)

# =========================
# Prediction
# =========================
if st.button("Predict Insurance Cost 💸"):

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Insurance Cost: ₹ {round(prediction, 2)}")

    # Extra insights
    if smoker == "yes":
        st.warning("⚠️ Smoking significantly increases insurance costs.")

    if bmi > 30:
        st.info("💡 Higher BMI may lead to higher charges.")

# =========================
# Footer
# =========================
st.divider()
st.markdown("Built by Soham Gore 🚀")
