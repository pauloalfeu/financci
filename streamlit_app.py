import streamlit as st
import numpy as np
import pandas as pd


st.markdown("""
## Bem-vindo ao seu Analisador de Rendimentos!

Este aplicativo te ajudará a analisar os seus rendimentos bancários de forma rápida e eficiente.

**Como utilizar:**

1. **Prepare seu arquivo:**
   * Certifique-se de que seu arquivo está no formato .txt.
   * Cada linha do arquivo deve conter as informações de um rendimento, separadas por vírgulas ou outro delimitador (por exemplo: data, valor, descrição).
   * **Exemplo:**
     ```
     01/01/2023,1000.50,Juros
     15/01/2023,500.25,Dividendos
     ```

2. **Faça o upload do arquivo:**
   * Clique no botão "Upload de Arquivo" e selecione o arquivo .txt que você preparou.

3. **Visualize seus resultados:**
   * Após o upload, o aplicativo irá processar o arquivo e exibir um resumo dos seus rendimentos, incluindo gráficos e tabelas.

**Observações:**

* **Formato do arquivo:** O formato do arquivo é crucial para o correto funcionamento do aplicativo. Por favor, verifique se o seu arquivo está no formato especificado.
* **Delimitadores:** Se os dados do seu arquivo estiverem separados por outro caractere além da vírgula, você pode ajustar o código do aplicativo para processar o arquivo corretamente.

**Dúvidas?** 
Entre em contato com o desenvolvedor.
""")

st.divider()






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

                # Convertendo a coluna 'RENDIMENTO LÍQUIDO' para float
                def limpar_e_converter(valor):
                    valor_str = str(valor)
                    # Remove todos os pontos, exceto o último
                    valor_str = valor_str.rstrip('.')  # Remove pontos no final
                    valor_str = valor_str.replace('.', '', valor_str.count('.') - 1)
                    # Substitui a vírgula por ponto
                    valor_str = valor_str.replace(',', '.')
                    # Remove espaços em branco
                    valor_str = valor_str.strip()
                    try:
                        return float(valor_str)
                    except ValueError:
                        print(f"Erro ao converter {valor} para float.")
                        return np.nan

                df_final['RENDIMENTO LÍQUIDO'] = df_final['RENDIMENTO LÍQUIDO'].apply(limpar_e_converter)

                for conta in contas_unicas:
                    # Filtrar o DataFrame para a conta atual
                    df_conta = df_final[df_final['CONTA'] == conta]

                    # Calcular o total de rendimentos líquidos para a conta
                    total_rendimento = df_conta['RENDIMENTO LÍQUIDO'].sum()

                    # Exibir os resultados no Streamlit
                    st.write("Dados da conta " + conta)
                    st.write("Total de Rendimentos Líquidos: R$ " + str(total_rendimento))
                    st.dataframe(df_conta)
            except Exception as e:
                st.error(f"Ocorreu um erro ao concatenar os DataFrames: {e}")
        else:
            st.info("Selecione os arquivos que deseja processar clicando no botão \"Browse files\" acima.")
#    except Exception as e:
#        st.error("Ocorreu um erro inesperado com um dos arquivos enviados. Por favor, tente novamente.")
