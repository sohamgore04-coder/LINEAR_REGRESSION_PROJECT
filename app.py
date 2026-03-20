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

# DEBUG (remove later)
st.write("Model expects:", model.feature_names_in_)

st.markdown("---")

# =========================
# Inputs
# =========================
age = st.number_input("Age", 18, 100, 25)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Children", 0, 5, 0)

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
if st.button("Predict 💸"):

    try:
        # =========================
        # One-Hot Encoding (CORRECT)
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

        # =========================
        # STRICT ALIGNMENT (KEY FIX)
        # =========================
        input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)

        # =========================
        # Prediction
        # =========================
        prediction = model.predict(input_df)[0]

        st.success(f"Estimated Cost: ₹ {round(prediction, 2)}")

        # Insights
        if smoker == "yes":
            st.warning("⚠️ Smoking increases cost significantly")
        if bmi > 30:
            st.info("💡 High BMI may increase cost")

    except Exception as e:
        st.error(f"Error: {e}")

# =========================
# Footer
# =========================
st.markdown("---")
st.caption("Built by Soham Gore 🚀")
