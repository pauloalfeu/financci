import streamlit as st


uploaded_file = st.file_uploader("Add text file !")

if uploaded_file:
    linhas_limpas = []
    for line in uploaded_file:
        texto = line.decode('latin-1')
        # Remove caracteres especiais (ajuste conforme necessário)
        texto = texto.strip()
        linhas_limpas.append(texto)
        for line in texto:
        # Remover quebras de linha e espaços em branco (se necessário)
            line = line.strip()

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