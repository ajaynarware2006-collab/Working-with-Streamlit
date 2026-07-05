import streamlit as st

st.header("About Me")
col1,col2=st.columns(2)
with col1:
    st.markdown("""
    * Collage :- IPS/IES ACEDEMY INDORE
    * Branch :- AIML
    * Current Semester :- 5th
    * Career goal :- Confidential
    * Current learning focus :- Streamlit
    """)

with col2:
    st.header("2 About Me")
    st.markdown("""
    * Collage :- IPS/IES ACEDEMY INDORE
    * Branch :- AIML
    * Current Semester :- 5th
    * Career goal :- Confidential
    * Current learning focus :- Streamlit
    """)

st.sidebar.selectbox(label="Select Branch",options=["AIML","CSE","EEE","Civil","chemical","FT"])

tab1,tab2=st.tabs(
    ["Overview","Chats"]
)