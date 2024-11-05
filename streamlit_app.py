import streamlit as st
import re

uploaded_file = st.file_uploader("Add text file !")
if uploaded_file:
    for line in uploaded_file:
        # Remover quebras de linha e espaços em branco (se necessário)
        line = line.strip()

        # Expressões regulares para extrair os dados
        conta = re.search(r'Conta:\s+(\S+)', line)
        mes_ano = re.search(r'Mês/ano referência:\s+(\S+)', line)
        rendimento = re.search(r'RENDIMENTO LÍQUIDO\s+(\S+)', line)

        if conta and mes_ano and rendimento:
            dados.append([conta.group(1), mes_ano.group(1), rendimento.group(1)])
        else:
            print(f"Linha não processada: {linha}")

        # Criar o DataFrame
        df = pd.DataFrame(dados, columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])
        #st.write(line)
        st.dataframe(df)

# update