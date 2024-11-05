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

        for line in texto:
            line = line.strip()

            # Dividindo a linha em partes usando espaços como delimitador
            partes = line.split()

            # Encontrando os índices das palavras-chave
            indice_conta = line.index('Conta:') + 1
            indice_mes_ano = line.index('Mês/ano') + 1
            indice_rendimento = line.index('RENDIMENTO') + 1

            # Extraindo os dados
            conta = partes[indice_conta]
            mes_ano = partes[indice_mes_ano]
            rendimento = partes[indice_rendimento]
            
            dados.append([conta, mes_ano, rendimento])

            df = pd.DataFrame(dados, columns=['CONTA', 'Mês/ano referência', 'RENDIMENTO LÍQUIDO'])
