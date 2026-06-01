import streamlit as st
import pickle
import numpy as np
import pandas as pd

# page config - must be first
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

# load model
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

# title
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b4b;'>
    ❤️ Heart Disease Prediction System
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("Enter patient details to check heart disease risk.")
st.divider()

# layout columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 20, 80, 40)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (0=Typical, 1=Atypical, 2=Non-Anginal, 3=Asymptomatic)", [0, 1, 2, 3])
    trestbps = st.slider("Resting Blood Pressure", 90, 200, 120)
    chol = st.slider("Cholesterol", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1=Yes, 0=No)", [0, 1])

with col2:
    restecg = st.selectbox("Rest ECG (0=Normal, 1=ST-T Abnormality, 2=LV Hypertrophy)", [0, 1, 2])
    thalach = st.slider("Max Heart Rate", 70, 210, 150)
    exang = st.selectbox("Exercise Angina (1=Yes, 0=No)", [0, 1])
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope (0=Upsloping, 1=Flat, 2=Downsloping)", [0, 1, 2])
    ca = st.selectbox("Major Vessels (0-4)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thal (1=Normal, 2=Fixed Defect, 3=Reversible Defect)", [1, 2, 3])

# convert sex to numeric
sex_value = 1 if sex == "Male" else 0

# prediction
if st.button("🔍 Predict Heart Disease"):

    data = pd.DataFrame(
        [[age, sex_value, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
        columns=["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
    )

    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]

    st.divider()

    if prediction[0] == 1:
        st.error("⚠ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    col3, col4 = st.columns(2)
    with col3:
        st.metric("Disease Probability", f"{round(probability * 100, 2)}%")
    with col4:
        st.metric("Healthy Probability", f"{round((1 - probability) * 100, 2)}%")

    st.divider()

st.caption("Machine Learning Model: Random Forest")
