import streamlit as st

st.title("Ajay Narware")
st.write("Indore, Madhya Pradesh")
st.write("")
st.subheader("AI Engineer Aspirant, Python Developer")
st.write("")
st.write("""Python developer with hands-on experience in data analysis and automation, pursuing B.Tech in Computer Science (AI & ML).
Looking to contribute to a Python internship role where I can apply skills in data analysis, object-oriented programming, and
problem-solving to build impactful applications""")
st.write("")
st.header("About Me")
st.markdown("""
* Collage :- IPS/IES ACEDEMY INDORE
* Branch :- AIML
* Current Semester :- 5th
* Career goal :- Confidential
* Current learning focus :- Streamlit
""")
st.write("")
st.header("Skills")
st.markdown("""
* Python
* PostgreSQL
* HTML/CSS
* Pandas
* Numpy
""")
st.write("")

st.header("EDUCATION")
st.write("""Bachelor of Technology (B.Tech) – Computer Science & Engineering (AI & ML)
IPS Academy, Indore
""")
st.write()

st.header("Code Example")

st.code("""import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import requests as rq
import streamlit as st
import os
import time
import psycopg as pg
from user_operation import user_login,user_signup
from dashboard import dashboard
from expense import add_expense,view_expense,delete_expense,update_expense
from report import show_report""")

st.divider()
st.caption("Thasts all i have till now.")
