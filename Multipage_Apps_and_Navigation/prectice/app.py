import streamlit as st

home=st.Page("home.py",title="Home")

analytics=st.Page("analytics.py",title="Analytics")

employee=st.Page("employees.py",title="Employee")

settings=st.Page("settings.py",title="Setting")

app=st.navigation([
    home,
    analytics,
    employee,
    settings
])

app.run()
