import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Escolha um arquivo .txt", type=["txt"])

if uploaded_file is not None:
    minha_lista = uploaded_file
    df = pd.read_csv(minha_lista, sep='\s+')  # Ajustar o separador se necessário
    st.dataframe(df)