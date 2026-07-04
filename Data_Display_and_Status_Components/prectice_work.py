#AI Analytics Dashboard
import streamlit as st
import time

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric(label="Revenue",value="3Cr")
with col2:
    st.metric(label="Active User",value="20M")
with col3:
    st.metric(label="Ai Predication",value="99.006")
with col4:
    st.metric(label="Customer Satisfaction",value="4")

model_details=({
    "Model Name":"",
    "Verson":"",
    "Accuracy":"",
    "Framework":"",
    "Last Update":""
})
st.json(model_details)

st.error("Model not found.")
st.warning("Dataset contains missing values.")
st.success("Prediction Completed")
st.info("Upload a CSV file.")

model_training=st.progress(0)
for i in range(101):
    model_training.progress(i)
    time.sleep(0.05)

st.spinner("Loading...")
time.sleep(2)
st.write("Your model is ")

import streamlit as st
import time

st.title("Status Demo")

with st.status(label="Running Processing...", expanded=True) as status:
    st.write("Loading dataset...")
    time.sleep(1)

    st.write("Cleaning data...")
    time.sleep(1)

    st.write("Training model...")
    time.sleep(1)

    st.write("Evaluating Model...")
    time.sleep(1)

    st.write("Saving model...")
    time.sleep(1)

    status.update(label="Process Completed", state="complete")
