import sys # importar e utilizar ferramentas do sistema
import os # importar e ter acesso ao sistema operacional

# direcionamento de caminhos e acesso a diretorios do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st 
from src.extract import extract_text_from_pdf
from src.gemini_api import ask_gemini

# Titulo da Aplicação
st.title("Gemini")

# Upload do arquivo PDF
upload_file = st.file_uploader("Faça upload de um PDF", type=["pdf"])

# Se um arquivo for carregado, extrai o texto e armazena ne sessão
if upload_file is not None:
    text = extract_text_from_pdf(upload_file)
    st.session_state["context"] = text

# Campo de entrada para a pergunta do usuario
question = st.text_input("Digite uma pergunta👍:")

# Se houver uma pergunta e um contexto carregado, chama a API do GEMINI!
if question and "context" in st.session_state:
    response = ask_gemini(question, st.session_state["context"])
    st.write("### Resposta:")
    st.write(response) # Exibe a resposta gerada pelo GEMINI!


