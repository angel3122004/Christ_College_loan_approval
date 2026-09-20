import streamlit as st
import joblib
import pandas as pd

# Load the trained Decision Tree model

model = joblib.load("loan_approval_decision_tree.pkl")

# Title

st.title("Loan Approval Prediction")
st.subheader("Decision Tree")

# Input: Income

income = st.number_input(
"Income",
min_value=0,
value=50000
)

# Input: Credit Score

credit_score = st.number_input(
"Credit Score",
min_value=0,
max_value=900,
value=720
)

# Prediction button

if st.button("Predict Loan Approval"):

```
# Create input data
new_applicant = pd.DataFrame({
    "Income": [income],
    "Credit_Score": [credit_score]
})

# Make prediction
prediction = model.predict(new_applicant)

# Display result
if prediction[0] == "YES":
    st.success("Prediction: LOAN APPROVED")
else:
    st.error("Prediction: LOAN NOT APPROVED")
