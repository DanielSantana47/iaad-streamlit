import streamlit as st
import pandas as pd
from database import get_db_connection  # Importando corretamente

st.set_page_config(page_title="User Data", page_icon="📊", layout="wide")

st.title("📊 User Data Overview")

# Obter conexão com o banco
connection = get_db_connection()

if connection:
    cursor = connection.cursor()

    # Buscar os dados da tabela "users"
    cursor.execute(
        "SELECT ID_Programador, Nome_Programador, Data_Nasc_Programador FROM programador")
    result = cursor.fetchall()
    connection.close()

    if result:
        # Criar um DataFrame do Pandas para exibir os dados
        df = pd.DataFrame(result, columns=[
                          "ID_Programador", "Nome_Programador", "Data_Nasc_Programador"])

        # Exibir os dados em uma tabela interativa
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No records found in the database.")

else:
    st.error("Database connection failed")
