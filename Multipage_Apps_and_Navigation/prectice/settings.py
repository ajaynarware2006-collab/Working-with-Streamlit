import streamlit as st

st.radio(label="Theme",options=["Dark","Light"])

st.selectbox(label="Language",options=["English","Hindi"])

st.checkbox(label="Notification")

st.button("Save")