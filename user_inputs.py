import streamlit as st

st.header("Personal Information")
name=st.text_input(label="Full Name",placeholder="Enter your Full Name")

email=st.text_input(label="Email",placeholder="@gmail.com")

age=st.number_input(label="Enter Age",min_value=0,max_value=110)

gender=st.radio(label="Gender",options=["Male","Female","Other"])

dob=st.date_input(label="Date of Birth")

time=st.time_input(label="Preferred Interview Time")


st.header("Education")
college=st.text_input(label="College Name",placeholder="Ex-IPS ACEDEMY INDORE")

branch=st.selectbox(label="Select Branch",options=["AIML","CSE","EEE","Civil","chemical","FT"])

current_semester=st.slider(label="Current Semester",min_value=1,max_value=8)


st.header("Technical Skills")

skills=st.multiselect(label="Choose",options=["python","java","c++","javascript","SQL"])

st.header("Career")
choice=st.radio(label="Preferred Role",options=["AI Engineer","Data Scientist","Backend Developer","Full Stack Developer"])

st.subheader("About Youself")
about=st.text_area(label="Why should we hire you?",max_chars=300)

check=st.checkbox("I confirm that all information is correct")

clicked=st.button("Submit")
