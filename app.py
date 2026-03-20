import streamlit as st
import joblib
import pandas as pd
import os

# =========================
# Load Model Safely
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(model_path)

# =========================
# Hardcoded Columns (Match Training)
# =========================
columns = [
    'age',
    'bmi',
    'children',
    'sex_male',
    'smoker_yes',
    'region_northwest',
    'region_southeast',
    'region_southwest'
]

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
# Inputs (Numeric Style)
# =========================
age = st.number_input("Age", min_value=18, max_value=100, value=25)

bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)

children = st.number_input("Number of Children", min_value=0, max_value=5, value=0)

sex = st.number_input("Gender (0 = Female, 1 = Male)", min_value=0, max_value=1, value=1)

smoker = st.number_input("Smoker (0 = No, 1 = Yes)", min_value=0, max_value=1, value=0)

region = st.number_input(
    "Region (0 = Northeast, 1 = Northwest, 2 = Southeast, 3 = Southwest)",
    min_value=0,
    max_value=3,
    value=0
)

st.markdown("---")

# =========================
# Prediction
# =========================
if st.button("Predict Insurance Cost 💸"):

    try:
        # =========================
        # Convert Inputs → One-Hot Encoding
        # =========================
        input_dict = {
            "age": age,
            "bmi": bmi,
            "children": children,
            "sex_male": 1 if sex == 1 else 0,
            "smoker_yes": 1 if smoker == 1 else 0,
            "region_northwest": 1 if region == 1 else 0,
            "region_southeast": 1 if region == 2 else 0,
            "region_southwest": 1 if region == 3 else 0,
        }

        input_df = pd.DataFrame([input_dict])

        # =========================
        # Align Columns
        # =========================
        input_df = input_df.reindex(columns=columns, fill_value=0)

        # =========================
        # Prediction
        # =========================
        prediction = model.predict(input_df)[0]

        st.success(f"Estimated Insurance Cost: ₹ {round(prediction, 2)}")

        # =========================
        # Insights (Professional Touch)
        # =========================
        if smoker == 1:
            st.warning("⚠️ Smoking significantly increases insurance costs.")

        if bmi > 30:
            st.info("💡 Higher BMI may lead to higher charges.")

        if age > 50:
            st.info("💡 Age is a strong factor in insurance pricing.")

    except Exception as e:
        st.error(f"Error: {e}")

# =========================
# Footer
# =========================
st.markdown("---")
st.caption("Built by Soham Gore 🚀")
