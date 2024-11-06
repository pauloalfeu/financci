import streamlit as st
import pandas as pd


#uploaded_file = st.file_uploader("Add text file !")
# Permite o upload de múltiplos arquivos
uploaded_files = st.file_uploader("Escolha os arquivos", accept_multiple_files=True)

# Processando os arquivos
if uploaded_files is not None:
    try:
        for uploaded_file in uploaded_files:
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
                    dados.append(numero_conta)
                    break  # Para o loop após encontrar a primeira ocorrência
                # Se não encontrar a linha "Conta:", imprime uma mensagem
                if 'numero_conta' not in locals():
                    st.error("A linha 'Conta:' não foi encontrada no DataFrame.")
            for index, row in df.iterrows():
                if 'Mês/ano' in row.values:
                    # Encontrou a linha com "Conta:"
                    mes_ano = row.iloc[row.values.tolist().index('Mês/ano') + 2]
                    dados.append(mes_ano)
                    break  # Para o loop após encontrar a primeira ocorrência
                # Se não encontrar a linha "Conta:", imprime uma mensagem
                if 'mes_ano' not in locals():
                    st.error("A linha 'mes_ano' não foi encontrada no DataFrame.")
            for index, row in df.iterrows():
                if 'LÍQUIDO' in row.values:
                    # Encontrou a linha com "Conta:"
                    rendimento = row.iloc[row.values.tolist().index('LÍQUIDO') + 1]
                    dados.append(rendimento)
                    break  # Para o loop após encontrar a primeira ocorrência
                # Se não encontrar a linha "Conta:", imprime uma mensagem
                if 'rendimento' not in locals():
                    st.error("A linha 'rendimento' não foi encontrada no DataFrame.")


            df = pd.DataFrame(columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])
            # Adicionando os dados da imagem ao DataFrame
            for i, valor in enumerate(dados):
                df.loc[0, df.columns[i]] = valor
            
            # Create 'mes' and 'ano' columns by splitting 'Mês/ano referência'
            df[['MÊS', 'ANO']] = df['Mês/ano referência'].str.split('/', expand=True)

            # Remove 'Mês/ano referência' column
            df = df.drop('Mês/ano referência', axis=1)


            st.data_editor(df)
    except Exception as e:
        st.error("Ocorreu um erro inesperado. Por favor, tente novamente mais tarde.")
