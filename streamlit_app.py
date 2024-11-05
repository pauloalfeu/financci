import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Escolha um arquivo .txt", type=["txt"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep='\t')  # Ajustar o separador se necessário
    st.dataframe(df)