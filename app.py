import streamlit as st
import joblib
import pandas as pd

model = joblib.load("loan_approval_decision_tree.pkl")

st.title("Loan Approval Prediction")
st.subheader("Decision Tree")

income = st.number_input("Income", min_value=0, value=50000)
credit_score = st.number_input("Credit Score", min_value=0, max_value=900, value=720)

if st.button("Predict Loan Approval"):
    data = [[income, credit_score]]
    prediction = model.predict(data)

    if prediction[0] == "YES":
        st.success("Loan Approved")
    else:
        st.error("Loan Not Approved")
