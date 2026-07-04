import streamlit as st

st.title("Image Demo")

st.image(
    "python.png",
    caption="View",
    width=400
)

audio = open("welcome.mp3","rb")

st.audio(audio)


video = open("demo.mp4","rb")

st.video(video)


st.download_button(
    label="Download Report",
    data="python.png",
    file_name="python.png",
    mime="image/png"
)

uploaded_file = st.file_uploader(
    "Upload your file"
)

if uploaded_file is not None:

    st.success("File Uploaded Successfully")

    st.write(uploaded_file.name)

    st.write(uploaded_file.type)

    st.write(uploaded_file.size)