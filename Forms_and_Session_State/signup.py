import streamlit as st

with st.form("sign_up"):
    st.markdown("<h1 style= color:red;text-align:center >Welcome to the app</h1>",unsafe_allow_html=True)


    name = st.text_input("Name")

    password = st.text_input("Password", type="password")

    confirm_pass= st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Sign up")

if submit:
    if not name:
        st.error("Plese Enter Your Name")
    
    elif not password and not confirm_pass:
        st.error("Password cannot be empty")

    elif password != confirm_pass:
        st.error("Password does not match")

    else:
        st.success("Login Successfully")


st.write("Alredy have an account")
if st.button("Login"):
    st.switch_page("pages/login.py")