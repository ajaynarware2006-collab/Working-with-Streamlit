from connection import connecting
import pandas as pd
import streamlit as st

connection,cursor=connecting()

query="SELECT * FROM user_view WHERE user_id=1;"
df=cursor.execute(query)

st.dataframe(df)

connection.close()
