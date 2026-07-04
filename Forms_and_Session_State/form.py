import streamlit as st

st.title("Student Registration Form")

with st.form("student_form"):

    name = st.text_input("Enter Name")

    age = st.number_input("Enter Age", min_value=16, max_value=60)

    branch = st.selectbox(
        "Branch",
        ["AIML","CSE","IT","ECE"]
    )

    submit = st.form_submit_button("Register")

if submit:

    st.success("Registration Successful!")

    st.write("Name :", name)
    st.write("Age :", age)
    st.write("Branch :", branch)



if "count" not in st.session_state:

    st.session_state.count = 0

if st.button("Increase"):

    st.session_state.count += 1

st.write(st.session_state.count)



if "number" not in st.session_state:

    st.session_state.number = 0

st.write(st.session_state.number)

if st.button("Increase"):

    st.session_state.number += 1

    st.rerun()