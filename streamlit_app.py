import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter



st.title("🎯 Financci")


################################### SEÇÃO DE UPLOAD DE DATAFRAME
st.divider()
st.markdown("##### Carregue um arquivo _.txt_ clicando em \"Browse files\" no campo abaixo:")
st.markdown("> **Importante:** siga as etapas apresentadas na guia **Tutorial de upload de arquivos** para fazer o download do arquivo correto.")
uploaded_file = st.file_uploader("")
if uploaded_file is not None:
    # Recebendo arquivo.txt:
    minha_lista = uploaded_file.readlines()
    st.markdown("Base de dados carregada com sucesso!")

    #dados = []
    for linha in minha_lista:
        # Remover quebras de linha e espaços em branco (se necessário)
        linha = linha.strip()

            # Dividindo a linha em partes usando espaços como delimitador
        partes = linha.split()

        """# Encontrando os índices das palavras-chave
        indice_conta = partes.index('Conta:') + 1
        indice_mes_ano = partes.index('Mês/ano') + 1
        indice_rendimento = partes.index('RENDIMENTO') + 1

        # Extraindo os dados
        conta = partes[indice_conta]
        mes_ano = partes[indice_mes_ano]
        rendimento = partes[indice_rendimento]

        dados.append([conta, mes_ano, rendimento])

        # Criar o DataFrame
    df = pd.DataFrame(dados, columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])
    
    # Create 'mes' and 'ano' columns by splitting 'Mês/ano referência'
    df[['MÊS', 'ANO']] = df['Mês/ano referência'].str.split('/', expand=True)

    # Remove 'Mês/ano referência' column
    df = dataframe.drop('Mês/ano referência', axis=1)
    # Create a copy of the dataframe
    df_copy = df.copy()

    # Combine the copied dataframe with the original dataframe 
    combined_df = pd.concat([df, df_copy], axis=0)"""

    if minha_lista.empty:
        print("DataFrame está vazio.")
    else:
        st.data_editor(minha_lista)