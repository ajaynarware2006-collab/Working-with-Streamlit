import streamlit as st
import pandas as pd


company_data = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Revenue": [120000,145000,138000,170000,182000,210000,225000,240000,260000,275000,295000,320000],
    "Expenses": [70000,76000,74000,90000,93000,105000,112000,118000,125000,133000,140000,150000],
    "Users": [1200,1350,1500,1700,1900,2150,2400,2700,3000,3400,3900,4500]
})
col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric(label="Revenue",value="3Cr")
with col2:
    st.metric(label="Expense",value="10L")
with col3:
    st.metric(label="Users",value="20M")
with col4:
    st.metric(label="Profit",value="2.9Cr")

st.dataframe(company_data)

st.bar_chart(company_data.set_index("Month"))

