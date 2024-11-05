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
    ################################### TRATAMENTO DO DATAFRAME
    def extrair_dados_lista(lista_linhas):
        """Extrai dados específicos de uma lista de strings e retorna um DataFrame.

        Args:
        lista_linhas: Uma lista de strings, onde cada string representa uma linha do arquivo.

        Returns:
        Um DataFrame com as colunas 'conta', 'Mês/ano referência' e 'RENDIMENTO LÍQUIDO'.
        """
        dados = []
        for linha in lista_linhas:
            # Remover quebras de linha e espaços em branco (se necessário)
            linha = linha.strip()

            # Expressões regulares para extrair os dados
            conta = re.search(r'Conta:\s+(\S+)', linha)
            mes_ano = re.search(r'Mês/ano referência:\s+(\S+)', linha)
            rendimento = re.search(r'RENDIMENTO LÍQUIDO\s+(\S+)', linha)

            if conta and mes_ano and rendimento:
                dados.append([conta.group(1), mes_ano.group(1), rendimento.group(1)])
            else:
                print(f"Linha não processada: {linha}")

            # Criar o DataFrame
        df = pd.DataFrame(dados, columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])
        return df

        """# Exemplo de uso:
        minha_lista = [
            "Conta: 45029-0 SIGTV410480820220001 GND3 Mês/ano referência: JANEIRO/2023 RENDIMENTO LÍQUIDO 1.362,38",
            # ... outras linhas ...
        ]"""

    def formatar_dados_df(dataframe):
        # prompt: Usando o DataFrame df: separar Mês e Ano e remover 'Mês/ano referência'

        # Create 'mes' and 'ano' columns by splitting 'Mês/ano referência'
        dataframe[['MÊS', 'ANO']] = dataframe['Mês/ano referência'].str.split('/', expand=True)

        # Remove 'Mês/ano referência' column
        dataframe = dataframe.drop('Mês/ano referência', axis=1)

        return dataframe

    def dataframe_combine(datafrane):
        # prompt: Usando o DataFrame df: fazer um cópia e combinar os dataframes

        # Create a copy of the dataframe
        df_copy = df.copy()

        # Combine the copied dataframe with the original dataframe 
        combined_df = pd.concat([df, df_copy], axis=0)

        return combined_df

    #################### CHAMANDHO AS FUNÇOES ##################################

    df = extrair_dados_lista(minha_lista)
    df = formatar_dados_df(df)


    if df.empty:
        print("DataFrame está vazio.")
    else:
        st.data_editor(df)