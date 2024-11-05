import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("Add text file !")

if uploaded_file:
    linhas_limpas = []

    for line in uploaded_file:
        texto = line.decode('latin-1')
        # Remove caracteres especiais (ajuste conforme necessário)
        texto = texto.strip()
        linhas_limpas.append(texto)
        
    palavras = []
    for line in linhas_limpas:
        line = line.strip()

        # Dividindo a linha em partes usando espaços como delimitador
        partes = line.split()
        palavras.append(partes)

    df = pd.DataFrame(palavras)

    # Iterando sobre as linhas do DataFrame
    dados = []
    for index, row in df.iterrows():
        if 'Conta:' in row.values:
            # Encontrou a linha com "Conta:"
            numero_conta = row.iloc[row.values.tolist().index('Conta:') + 1]
            dados.append([numero_conta.group(1)])
            break  # Para o loop após encontrar a primeira ocorrência
        # Se não encontrar a linha "Conta:", imprime uma mensagem
        if 'numero_conta' not in locals():
            print("A linha 'Conta:' não foi encontrada no DataFrame.")
    
    #st.write((type(linhas_limpas)))
    st.data_editor(dados)
