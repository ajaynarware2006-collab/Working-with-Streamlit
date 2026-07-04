import streamlit as st

st.title("AI Resume Analyzer")
st.write("This is just a UI that i have created by learning Media and file handling streamlit function")
st.image("python.png",caption="Company logo",width=100)

with st.sidebar:
    st.markdown("**App verson** : 5 PRO")
    st.markdown("**Devoloper Name** : Ajay")
    st.radio(label="Theme",options=["Dark","Light"])

upload=st.file_uploader("Upload your resume",type=["pdf","docx"])
if upload is not None:
    st.success("Flie successfully uploaded")
    st.write(upload.type)
    st.write(f"{upload.name} is Uploaded")

report = """
AI Resume Analyzer Report

Skills Found:
- Python
- SQL
- Git

Resume Score : 84%

Thank You
"""
st.download_button(label="Download report",data=report,file_name="Report.txt")