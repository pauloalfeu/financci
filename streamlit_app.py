import streamlit as st


uploaded_file = st.file_uploader("Add text file !")

if uploaded_file:
    linhas_limpas = []
    for line in uploaded_file:
        texto = line.decode('latin-1')
        # Remove caracteres especiais (ajuste conforme necessário)
        texto = texto.strip()
        linhas_limpas.append(texto)
        st.write(texto)