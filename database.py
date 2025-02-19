import os
import mysql.connector
import streamlit as st
from dotenv import load_dotenv  # Adicione esta importação

# Carrega variáveis do .env
load_dotenv()  # Não esqueça desta linha!

# Função para conectar ao banco de dados


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE'),
            port=3306,  # Adicione a porta explicitamente
            charset='utf8mb4',  # Evita problemas com caracteres especiais
            connect_timeout=10  # Timeout de conexão
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"🚨 Erro ao conectar ao banco de dados: {err}")
        st.error("Verifique se:")
        st.error("1. O MySQL está rodando")
        st.error("2. As credenciais estão corretas no arquivo .env")
        st.error("3. O usuário tem permissões de acesso")
        return None
