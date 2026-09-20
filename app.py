```python
import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("loan_approval_decision_tree.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("Loan Approval Prediction")
st.subheader("Decision Tree")

# Input fields
income = st.number_input(
    "Income",
    min_value=0,
    value=50000
)

credit_score = st.number_input(
    "Credit Score",
    min_value=0,
    max_value=900,
    value=720
)

# Prediction button
if st.button("Predict Loan Approval"):

    new_applicant = pd.DataFrame({
        "Income": [income],
        "Credit_Score": [credit_score]
    })

    prediction = model.predict(new_applicant)

    if prediction[0] == "YES":
        st.success("Prediction: LOAN APPROVED")
    else:
        st.error("Prediction: LOAN NOT APPROVED")
```
