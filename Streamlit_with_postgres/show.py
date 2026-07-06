from connection import connecting
import pandas as pd
import streamlit as st

connection=connecting()

query="SELECT * FROM user_view WHERE user_id=1;"
df=pd.read_sql(query,connection)


st.dataframe(df)

connection.close()
