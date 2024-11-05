import streamlit as st


uploaded_file = st.file_uploader("Add text file !")
uploaded_file.decode('utf-8')
if uploaded_file:
    for line in uploaded_file:
        st.write(line)