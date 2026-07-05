import pandas as pd
import streamlit as st

employee=pd.DataFrame({
    "Name":["Ajay","Rahul","bhumit","Someone"],
    "Department":["Ai","Data science","Backend","DevOps"],
    "Expriense":["5 Years","2 Years","1 Years","4 Years"]
})

st.dataframe(employee)