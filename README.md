# 💰 Medical Insurance Cost Prediction App

## 📌 Project Overview

This project is a machine learning web application that predicts medical insurance costs based on user inputs such as age, BMI, smoking habits, and region.

The model is trained on the Insurance dataset and deployed using **Streamlit** for real-time predictions.

---

## 🚀 Features

* User-friendly web interface
* Real-time insurance cost prediction
* Data preprocessing & feature engineering
* Machine Learning model (Linear Regression / Random Forest)
* Insights based on user input (e.g., smoking impact)

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit

---

## 📊 Input Parameters

* Age
* BMI
* Number of Children
* Gender
* Smoking Status
* Region

---

## 💻 How to Run Locally

```bash
git clone https://github.com/your-username/insurance-app.git
cd insurance-app
pip install -r requirements.txt
streamlit run app.py
```

### 🔹 Home Page

![Home Page](screenshots/home.png)

## 📈 Model Performance

* Training R² Score: ~0.85+
* Testing R² Score: ~0.80+
* Evaluation Metrics: MSE, R² Score

---

## ⚠️ Key Insights

* Smoking significantly increases insurance costs
* Higher BMI leads to higher charges
* Age has a strong positive correlation with cost

---

## 🌐 Deployment

The app is deployed using Streamlit Cloud.

🔗 Live App: https://your-app-link.streamlit.app

---
