import streamlit as st
import pandas as pd
import time

st.title("Line Chart Demo")

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [120, 180, 150, 210, 250]
})
st.line_chart(data.set_index("Month"))



st.title("Bar Chart Demo")

data = pd.DataFrame({
    "Language": ["Python", "Java", "C++", "JavaScript"],
    "Students": [80, 45, 30, 60]
})

st.bar_chart(data.set_index("Language"))


st.title("Area Chart Demo")

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Users": [100, 150, 220, 280, 340]
})

st.area_chart(data.set_index("Month"))

import matplotlib.pyplot as plt

st.title("Matplotlib Demo")

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 6, 5]

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_title("Sample Plot")

st.pyplot(fig)


import plotly.express as px

st.title("Plotly Demo")

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Revenue": [12, 18, 15, 25, 30]
})

fig = px.line(
    df,
    x="Month",
    y="Revenue",
    title="Monthly Revenue"
)

st.plotly_chart(fig)