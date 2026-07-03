import streamlit as st

with st.sidebar:
    st.header("AI prediction platform")
    st.selectbox(label="Select Model",options=[
        "House Price Prediction",
        "Disease Prediction",
        "Resume Analyzer",
        "Sentiment Analysis"
    ])
    st.radio(label="Theme",options=[
        "Light",
        "Dark"
    ])
    st.checkbox("Enable Notification")

with st.container() as row1:
    col1,col2=st.columns([2,1])
    with col1:
        st.header("⚙️ Settings")
        st.write("This is a application that contain different AI prediction models")
    with col2:
        st.subheader("Model Version")
        st.write("5.5 PRO")
        st.subheader("Accuracy")
        st.write("89%")
        st.subheader("Last updated")
        st.write("Recently")

with st.container() as row2:
    col1,col2,col3=st.columns(3)
    with col1:
        st.markdown("**Total Predictions**")

    with col2:
        st.markdown("**Today's Users**")

    with col3:
        st.markdown("**Response Time**")

with st.container() as row3:
    tab1,tab2,tab3=st.tabs(
        ["Overview","Dataset","About Model"])
    with tab1:
        pass
    with tab2:
        pass
    with tab3:
        pass
    
with st.container() as row4:
    with st.expander("Advanced Settings"):
        st.slider(label="Confidence Threshold") 
        st.toggle(label="Enable GPU")
        st.number_input(label="Batch Size",placeholder="Enter Batch Size",value=int())
    
st.divider()
st.caption("Design AI dashboard layout using Streamlit layout components")