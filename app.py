import streamlit as st
import pickle
import numpy as np

# Load the model
with open("Logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Absenteeism Prediction App")
st.write("Predict whether an employee will be absent based on work & personal attributes.")

# Reason group input (One-hot encoded)
st.subheader("Reason for absence (Select one group)")
reason_group = st.selectbox("Reason Group", ["G0", "G1", "G2", "G3"])
reason_encoded = {
    "G0": [1, 0, 0, 0],
    "G1": [0, 1, 0, 0],
    "G2": [0, 0, 1, 0],
    "G3": [0, 0, 0, 1],
}[reason_group]

# Other input fields
day_of_week = st.slider("Day of the week (1=Monday, ..., 7=Sunday)", 1, 7, 1)
month = st.slider("Month", 1, 12, 1)
transport = st.number_input("Transportation Expense", min_value=0)
distance = st.number_input("Distance to Work (in km)", min_value=0)
age = st.number_input("Age", min_value=18)
workload_avg = st.number_input("Daily Work Load Average", min_value=0.0)
bmi = st.number_input("Body Mass Index", min_value=10)
education = st.radio("Education Level (0 = High School or lower, 1 = Higher Education)", [0, 1])
children = st.slider("Number of Children", 0, 10, 0)
pets = st.slider("Number of Pets", 0, 10, 0)

# Combine inputs
input_data = np.array([
    *reason_encoded,
    day_of_week,
    month,
    transport,
    distance,
    age,
    workload_avg,
    bmi,
    education,
    children,
    pets
]).reshape(1, -1)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    label = "Absent" if prediction == 1 else "Not Absent"
    st.success(f"Prediction: **{label}**")
