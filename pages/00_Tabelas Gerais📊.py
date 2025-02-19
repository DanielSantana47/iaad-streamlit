import streamlit as st
import pandas as pd
from database import get_db_connection  # Importando corretamente

st.set_page_config(page_title="📊 Tabelas do BD", page_icon="📊", layout="wide")

st.title("📊 Tabelas do BD")

# Obter conexão com o banco
connection = get_db_connection()

if connection:
    cursor = connection.cursor()

    # Exibir tabela de Programadores
    st.subheader("Programadores")
    cursor.execute(
        "SELECT ID_Programador, ID_Startup, Nome_Programador, Genero_Programador, Data_Nasc_Programador FROM programador"
    )
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=[
            "ID_Programador", "ID_Startup", "Nome_Programador", "Genero_Programador", "Data_Nasc_Programador"
        ])
        df = df.reset_index(drop=True)  # Remover índice automático
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Nenhum programador encontrado no banco de dados.")

    # Exibir tabela de Startups
    st.subheader("Startups")
    cursor.execute(
        "SELECT ID_Startup, Nome_Startup, Cidade_Sede FROM startup"
    )
    result = cursor.fetchall()

    if result:
        df_startup = pd.DataFrame(result, columns=[
            "ID_Startup", "Nome_Startup", "Cidade_Sede"
        ])
        df_startup = df_startup.reset_index(
            drop=True)  # Remover índice automático
        st.dataframe(df_startup, use_container_width=True)
    else:
        st.warning("Nenhuma startup encontrada no banco de dados.")

    # Exibir tabela de Linguagens
    st.subheader("Linguagens")
    cursor.execute(
        "SELECT ID_Linguagem, Nome_Linguagem FROM linguagem"
    )
    result = cursor.fetchall()

    if result:
        df_linguagem = pd.DataFrame(result, columns=[
            "ID_Linguagem", "Nome_Linguagem"
        ])
        df_linguagem = df_linguagem.reset_index(
            drop=True)  # Remover índice automático
        st.dataframe(df_linguagem, use_container_width=True)
    else:
        st.warning("Nenhuma linguagem encontrada no banco de dados.")

    # Exibir tabela de Programador_Linguagem
    st.subheader("Relação Programador - Linguagem")
    cursor.execute(
        "SELECT ID_Programador, ID_Linguagem FROM programador_linguagem"
    )
    result = cursor.fetchall()

    if result:
        df_programador_linguagem = pd.DataFrame(result, columns=[
            "ID_Programador", "ID_Linguagem"
        ])
        df_programador_linguagem = df_programador_linguagem.reset_index(
            drop=True)  # Remover índice automático
        st.dataframe(df_programador_linguagem, use_container_width=True)
    else:
        st.warning(
            "Nenhuma relação programador-linguagem encontrada no banco de dados.")

    # Exibir tabela de Dependentes
    st.subheader("Dependentes")
    cursor.execute(
        "SELECT ID_Dependente, ID_Responsavel, Parentesco_Dependente, Data_Nasc_Dependente FROM dependente"
    )
    result = cursor.fetchall()

    connection.close()

    if result:
        df_dependente = pd.DataFrame(result, columns=[
            "ID_Dependente", "ID_Responsavel", "Parentesco_Dependente", "Data_Nasc_Dependente"
        ])
        df_dependente = df_dependente.reset_index(
            drop=True)  # Remover índice automático
        st.dataframe(df_dependente, use_container_width=True)
    else:
        st.warning("Nenhum dependente encontrado no banco de dados.")

else:
    st.error("Falha na conexão com o banco de dados.")
