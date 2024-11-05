import streamlit as st


uploaded_file = st.file_uploader("Add text file !")

if uploaded_file:
    for line in uploaded_file:
        texto = line.decode('utf-8')
        # Remove caracteres especiais (ajuste conforme necessário)
        texto = texto.strip()
        linhas_limpas.append(texto)
        st.write(texto)