import streamlit as st
import pandas as pd

#uploaded_file = st.file_uploader("Add text file !")
# Permite o upload de múltiplos arquivos
uploaded_files = st.file_uploader("", accept_multiple_files=True)

# Lista para armazenar os DataFrames
all_dfs = []

# Processando os arquivos
if uploaded_files is not None:
#    try:
        for uploaded_file in uploaded_files:
            try:
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

                encontrado = False
                for index, row in df.iterrows():
                    if 'Conta:' in row.values:
                        # Encontrou a linha com "Conta:"
                        numero_conta = row.iloc[row.values.tolist().index('Conta:') + 1]
                        dados.append(numero_conta)
                        encontrado = True
                        break  # Para o loop após encontrar a primeira ocorrência
                if not encontrado:
                    st.error("'Conta' não foi encontrada no ", uploaded_file.name)
                for index, row in df.iterrows():
                    if 'Mês/ano' in row.values:
                        # Encontrou a linha com "Conta:"
                        mes_ano = row.iloc[row.values.tolist().index('Mês/ano') + 2]
                        dados.append(mes_ano)
                        encontrado = True
                        break  # Para o loop após encontrar a primeira ocorrência
                if not encontrado:
                    st.error("'Mês/ano' não foi encontrado no ", uploaded_file.name)
                for index, row in df.iterrows():
                    if 'LÍQUIDO' in row.values:
                        # Encontrou a linha com "Conta:"
                        rendimento = row.iloc[row.values.tolist().index('LÍQUIDO') + 1]
                        dados.append(rendimento)
                        encontrado = True
                        break  # Para o loop após encontrar a primeira ocorrência
                if not encontrado:
                    st.error("'Rendimento' não foi encontrado no ", uploaded_file.name)



                df = pd.DataFrame(columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])
                # Adicionando os dados da imagem ao DataFrame
                for i, valor in enumerate(dados):
                    df.loc[0, df.columns[i]] = valor
                
                # Create 'mes' and 'ano' columns by splitting 'Mês/ano referência'
                df[['MÊS', 'ANO']] = df['Mês/ano referência'].str.split('/', expand=True)

                # Remove 'Mês/ano referência' column
                df = df.drop('Mês/ano referência', axis=1)


                #st.data_editor(df)
                # Adicionar o DataFrame à lista com todos
                all_dfs.append(df)
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado com o arquivo: \"{uploaded_file.name}\" presente nos arquivos enviados. Por favor, verifique-o e tente novamente.")

        # Concatenar todos os DataFrames, se houver pelo menos um
        if all_dfs:
            try:
                df_final = pd.concat(all_dfs, ignore_index=True)
                contas_unicas = df_final['CONTA'].unique()
                #st.write(df_final)
                for conta in contas_unicas:
                    # Filtrar o DataFrame para a conta atual
                    df_conta = df_final[df_final['CONTA'] == conta]

                    # Exibir o DataFrame da conta atual
                    st.write(f"Dados da conta {conta}")
                    st.dataframe(df_conta)
            except Exception as e:
                st.error(f"Ocorreu um erro ao concatenar os DataFrames: {e}")
        else:
            st.info("Selecione os arquivos que deseja processar clicando no botão \"Browse files\" acima.")
#    except Exception as e:
#        st.error("Ocorreu um erro inesperado com um dos arquivos enviados. Por favor, tente novamente.")
