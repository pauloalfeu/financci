import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter



st.title("🎯 Financci")


################################### SEÇÃO DE UPLOAD DE DATAFRAME
st.divider()
st.markdown("##### Carregue um arquivo _.txt_ clicando em \"Browse files\" no campo abaixo:")
st.markdown("> **Importante:** siga as etapas apresentadas na guia **Tutorial de upload de arquivos** para fazer o download do arquivo correto.")
uploaded_file = st.file_uploader()
if uploaded_file is not None:
    # Recebendo arquivo.txt:
    #minha_lista = uploaded_file.readlines()
    st.markdown("Base de dados carregada com sucesso!")

    st.data_editor(minha_lista)