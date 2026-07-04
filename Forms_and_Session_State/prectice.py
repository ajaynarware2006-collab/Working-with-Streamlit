#AI Chat Interface
import streamlit as st

questions = [
    "",
    "What is Machine Learning?",
    "Explain Neural Networks",
    "What is Streamlit?",
    "Difference between AI and ML?",
    "Explain FastAPI"
]

with st.sidebar:
    st.radio(label="Theme",options=["Dark","Light"])
    st.slider(label="Tempreture",max_value=100,min_value=-20)
    st.button(label="Clear Chat")

with st.form("Query"):
    name=st.text_input(label="User Name",placeholder="Enter your Name")
    ques=st.selectbox(label="Select your Query",options=questions)
    custom_ques=st.text_area("Ask your own question")


    ask=st.form_submit_button("Ask")
if ask:
    st.write(f"Name : {name}")
    if ques:
        st.write(f"Selcted Question : {ques}")
    else:
        st.write(f"Custom Question : {custom_ques}")

    
