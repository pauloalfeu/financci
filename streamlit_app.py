import streamlit as st


uploaded_file = st.file_uploader("Add text file !")

if uploaded_file:
    linhas_limpas = []

    for line in uploaded_file:
        texto = line.decode('latin-1')
        # Remove caracteres especiais (ajuste conforme necessário)
        texto = texto.strip()
        linhas_limpas.append(texto)
        
    dados = []
    for line in linhas_limpas:
        line = line.strip()

        # Dividindo a linha em partes usando espaços como delimitador
        partes = line.split()

    for chave, palavra in linhas_limpas:
        if palavra == "Conta:":
            conta = palavra
            dados.append([conta.group(1)])
        else:
            st.write("Não encontrado 'Conta:' na posição esperada.")

    #dados.append([conta.group(1), mes_ano.group(1), rendimento.group(1)])

    # Criar o DataFrame
    df = pd.DataFrame(dados, columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])

    st.data_editor(df)
