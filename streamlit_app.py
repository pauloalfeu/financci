import streamlit as st

uploaded_file = st.file_uploader("Add text file !")
if uploaded_file:
    dados=[]
    for line in uploaded_file:
        # Encontrando os índices das palavras-chave
        indice_conta = line.index("b'Conta:") + 1
        indice_mes_ano = line.index("b'M\xeas/ano refer\xeancia:") + 1
        indice_rendimento = line.index("b'RENDIMENTO L\xcdQUIDO") + 1

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