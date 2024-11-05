import streamlit as st

uploaded_file = st.file_uploader("Add text file !")
if uploaded_file:
    dados=[]
    for line in uploaded_file:
        partes = line.split()

        # Encontrando os índices das palavras-chave
        indice_conta = partes.index('Conta:\s+(\S+)') + 1
        indice_mes_ano = partes.index('Mês/ano referência:\s+(\S+)') + 1
        indice_rendimento = partes.index('RENDIMENTO LÍQUIDO\s+(\S+)') + 1

        # Extraindo os dados
        conta = partes[indice_conta]
        mes_ano = partes[indice_mes_ano]
        rendimento = partes[indice_rendimento]

        dados.append([conta, mes_ano, rendimento])

        # Criar o DataFrame
        df = pd.DataFrame(dados, columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])
        #st.write(line)
        st.dataframe(df)

# update