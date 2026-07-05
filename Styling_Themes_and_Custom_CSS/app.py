import streamlit as st

st.set_page_config(
    page_title="AI Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://docs.streamlit.io",
        "Report a Bug": "https://github.com/streamlit/streamlit",
        "About": "This is my first professional Streamlit application."
    }
)

st.title("Advanced Page Config")


st.markdown("""
<style>

    .big-title{

        font-size:55px;

        color:black;

        text-align:center;

    }

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<h1 class="big-title">
AI Dashboard
</h1>
""",
unsafe_allow_html=True
)

st.markdown("""
<div style="
padding:20px;
border-radius:15px;
background:#1E1E1E;
">

<h2>Revenue</h2>

<h1>₹2,50,000</h1>

</div>
""",
unsafe_allow_html=True)