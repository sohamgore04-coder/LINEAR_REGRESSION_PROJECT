import streamlit as st
import joblib
import pandas as pd
import os

# =========================
# Load Model
# =========================
current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "model.pkl")
model = joblib.load(model_path)

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰"
)

# =========================
# Title
# =========================
st.title("💰 Medical Insurance Cost Prediction")
st.write("Enter details to estimate the **insurance charges**.")

st.markdown("---")

# =========================
# Numeric-style Inputs
# =========================

age = st.number_input("Age", min_value=18, max_value=100, value=25)

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)

children = st.number_input("Number of Children", min_value=0, max_value=5, value=0)

# Instead of dropdown → numeric encoding
sex = st.number_input("Gender (0 = Female, 1 = Male)", min_value=0, max_value=1, value=1)

smoker = st.number_input("Smoker (0 = No, 1 = Yes)", min_value=0, max_value=1, value=0)

# Region encoding (simple numeric)
region = st.number_input(
    "Region (0 = Northeast, 1 = Northwest, 2 = Southeast, 3 = Southwest)",
    min_value=0,
    max_value=3,
    value=0
)

st.markdown("---")

# =========================
# Prepare Input
# =========================
# IMPORTANT: Must match training format

input_data = pd.DataFrame([{
    "age": age,
    "bmi": bmi,
    "children": children,
    "sex": sex,
    "smoker": smoker,
    "region": region
}])

# =========================
# Prediction
# =========================
if st.button("Predict Insurance Cost 💸"):

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Insurance Cost: ₹ {round(prediction, 2)}")

    # Insights (industry touch 🔥)
    if smoker == 1:
        st.warning("⚠️ Smoking increases insurance cost significantly.")

    if bmi > 30:
        st.info("💡 High BMI may lead to higher charges.")

    if age > 50:
        st.info("💡 Age is a strong factor in cost increase.")

# =========================
# Footer
# =========================
st.markdown("---")
st.caption("Built by Soham Gore 🚀")
