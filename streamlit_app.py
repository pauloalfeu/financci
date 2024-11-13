import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Calculador de Rendimentos")

with st.sidebar:
    st.title("Instruções")
    st.write("Abaixo apresentamos um guia rápido sobre como usar o aplicativo.")

    # Adicione aqui o seu tutorial completo, utilizando markdown
    st.markdown("""
    **Passo a passo:**

    1. **Carregar o arquivo:** Clique no botão "Browse files" e selecione um ou mais arquivos .txt de rendimentos do seu computador.
    2. **Selecionar as colunas:** Clique na caixa de seleção (no nome das colunas) para escolher ordenar os dados da maneira que deseja analisar.
    3. **Visualizar os resultados:** As tabelas e os somatórios serão exibidos abaixo, separados por conta bancária.
    4. **Faça o download das tabelas:** Se desejar, é possível baixar as tabelas individualmente. Para isso, passe o cursor do mouse sobre a tabela desejada e clique no ícone de download.
    
    """)


st.markdown("<h1 style='color: rgb(0, 66, 128); text-align: center;'> 📝 Calculador de Rendimentos</h1>", unsafe_allow_html=True)
st.markdown("""

Este aplicativo te ajudará a analisar os seus rendimentos bancários de forma rápida e eficiente.

**Observações:**

* **Formato do arquivo:** O formato do arquivo é crucial para o correto funcionamento do aplicativo. Por favor, verifique se o seu arquivo está no formato especificado _(.txt)_.
* **Erro comum:** Grande parte das mensagens de erro podem indicar que o arquivo enviado não possui dados para leitura, por não haver rendimentos no período indicado (tente verificar no aplicativo bancário se realmente houve rendimento).

""")

st.info("**Problema com o arquivo?** Se você ver uma mensagem de erro, é provável que o arquivo tenha um formato inesperado. Clique no **'X'** para removê-lo e tente novamente.")

st.markdown("""
**Dúvidas extras?** Entre em contato com o desenvolvedor.

-----
""")
#st.divider()






#uploaded_file = st.file_uploader("Add text file !")
# Permite o upload de múltiplos arquivos
st.warning("""
    **Aviso:** Os dados que você enviar serão processados apenas durante o uso do aplicativo e **não serão armazenados**, garantindo a sua privacidade e a segurança de suas informações.
    """)
uploaded_files = st.file_uploader("**Adicione os arquivos aqui:**", accept_multiple_files=True)

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
                    valor_str = valor_str.rstrip('.')  # Remove pontos no final
                    # Substitui a vírgula por ponto
                    valor_str = valor_str.replace(',', '.')
                    # Remove todos os pontos, exceto o último
                    valor_str = valor_str.replace('.', '', valor_str.count('.') - 1)
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
                    st.divider()
                    st.write("Dados da conta " + conta)
                    st.markdown("**Total de Rendimentos Líquidos: R$" + str("{:.2f}".format(total_rendimento)) + "**")
                    st.dataframe(df_conta)
            except Exception as e:
                st.error(f"Ocorreu um erro ao concatenar os DataFrames: {e}")
        else:
            st.info("Selecione os arquivos que deseja processar clicando no botão \"Browse files\" acima.")
#    except Exception as e:
#        st.error("Ocorreu um erro inesperado com um dos arquivos enviados. Por favor, tente novamente.")
