import streamlit as st
import time

st.metric(label="Income" , value="₹250000",delta="+15%")
st.metric(
    label="Model Accuracy",
    value="97.8%",
    delta="+0.6%",
    border=True
)

import pandas as pd

df = pd.DataFrame({
    "Name": ["Ajay", "Rahul", "Priya"],
    "Age": [20, 21, 19],
    "Branch": ["AIML", "CSE", "IT"]
})

st.title("st.dataframe() Demo")

st.dataframe(df)


table = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost", "SVM"],
    "Accuracy": ["94%", "96%", "91%"]
})

st.title("st.table() Demo")

st.table(table)


user = {
    "name": "Ajay",
    "age": 20,
    "skills": [
        "Python",
        "PostgreSQL",
        "Streamlit"
    ],
    "college": {
        "name": "IPS Academy",
        "branch": "AIML"
    }
}

st.title("st.json() Demo")

st.json(user)

st.error("Model not found.")
st.warning("Dataset contains missing values.")
st.success("Prediction Completed")
st.info("Upload a CSV file.")

st.progress(89)

with st.spinner("Loading..."):
    time.sleep(3)


st.title("Status Demo")

with st.status("Running AI Pipeline...", expanded=True) as status:
    st.write("Loading dataset...")
    time.sleep(1)

    st.write("Cleaning data...")
    time.sleep(1)

    st.write("Training model...")
    time.sleep(1)

    st.write("Saving model...")
    time.sleep(1)

    status.update(label="Pipeline Completed", state="complete")
