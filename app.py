import streamlit as st
import joblib
import pandas as pd
import os

# =========================
# Load Model
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

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
# Inputs
# =========================
age = st.number_input("Age", 18, 100, 25)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Number of Children", 0, 5, 0)

sex = st.selectbox("Gender", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

st.markdown("---")

# =========================
# Prediction
# =========================
if st.button("Predict Insurance Cost 💸"):

    try:
        # One-hot encoding
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

        # Align features
        input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

        # Predict
        prediction = model.predict(input_df)

        # FINAL FIX HERE
        prediction_value = float(prediction.flatten()[0])

        # Output
        st.success(f"Estimated Insurance Cost: ₹ {round(prediction_value, 2)}")

        # Insights
        if smoker == "yes":
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
