import streamlit as st

st.set_page_config(
    page_title="AI Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to AI Dashboard")

home = st.Page("home.py", title="Home")

dashboard = st.Page(
    "dashboard.py",
    title="Dashboard"
)

setting = st.Page(
    "setting.py",
    title="Setting"
)

pg = st.navigation(
    [
        home,
        dashboard,
        setting
    ]
)

pg.run()