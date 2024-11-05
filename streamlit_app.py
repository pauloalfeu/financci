import streamlit as st


uploaded_file = st.file_uploader("Add text file !")

if uploaded_file:
    linhas_limpas = []

    for line in uploaded_file:
        texto = line.decode('latin-1')
        # Remove caracteres especiais (ajuste conforme necessário)
        texto = texto.strip()
        linhas_limpas.append(texto)
        
        dados = []

    for line in linhas_limpas:
        line = line.strip()

        # Dividindo a linha em partes usando espaços como delimitador
        partes = line.split()

        st.write(partes)
