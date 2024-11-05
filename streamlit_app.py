import streamlit as st


uploaded_file = st.file_uploader("Add text file !")
if uploaded_file:
    for line in uploaded_file:
        st.write(line)

# update