import streamlit as st
import pandas as pd
from database import get_db_connection  # Importando corretamente

st.set_page_config(page_title="HomePage",
                   page_icon="\U0001F3E0", layout="wide")

st.title("HomePage 🏠")
st.write("Nesta página, você encontrará visualizações de dados informativas, explorando tanto os insights mais evidentes quanto os mais sutis que nosso banco de dados oferece.🚀")
# Obter conexão com o banco
connection = get_db_connection()

if connection:
    cursor = connection.cursor()

    st.subheader("Startups e Seus Funcionários 🏢")
    # Buscar os dados da tabela "startup" e "programador"
    cursor.execute("""
        SELECT s.Nome_Startup, 
               GROUP_CONCAT(p.Nome_Programador SEPARATOR ', ') AS Funcionarios
        FROM startup AS s
        LEFT JOIN programador AS p ON s.ID_Startup = p.ID_Startup
        GROUP BY s.Nome_Startup;
    """)
    result = cursor.fetchall()

    if result:
        df = pd.DataFrame(result, columns=["Nome_Startup", "Funcionarios"])
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

    st.subheader("Programadores e Linguagens que Atuam 👨‍💻")
    cursor.execute("""
        SELECT p.Nome_Programador, 
               GROUP_CONCAT(l.Nome_Linguagem SEPARATOR ', ') AS Linguagens
        FROM programador_linguagem AS pg
        INNER JOIN programador AS p ON pg.ID_Programador = p.ID_Programador
        INNER JOIN linguagem AS l ON pg.ID_Linguagem = l.ID_Linguagem
        GROUP BY p.Nome_Programador;
    """)
    result = cursor.fetchall()

    if result:
        df_pl = pd.DataFrame(
            result, columns=["Nome_Programador", "Linguagens"])
        st.dataframe(df_pl, use_container_width=True)
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

    st.subheader("Programadores e seus Dependentes 👨‍👩‍👦")
    cursor.execute("""
        SELECT p.Nome_Programador, d.Nome_Dependente, d.Parentesco_Dependente
        FROM programador AS p
        LEFT JOIN dependente AS d ON p.ID_Programador = d.ID_Responsavel
        WHERE d.Nome_Dependente IS NOT NULL;
    """)
    result = cursor.fetchall()

    if result:
        df_dep = pd.DataFrame(result, columns=[
                              "Nome_Programador", "Nome_Dependente", "Parentesco_Dependente"])
        st.dataframe(df_dep, use_container_width=True)
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

    st.subheader("Programadores sem Dependentes 🕴")
    cursor.execute("""
        SELECT p.Nome_Programador, d.Nome_Dependente
        FROM programador AS p
        LEFT JOIN dependente AS d ON p.ID_Programador = d.ID_Responsavel
        WHERE d.Nome_Dependente IS NULL;
    """)
    result = cursor.fetchall()

    if result:
        df_no_dep = pd.DataFrame(
            result, columns=["Nome_Programador", "Nome_Dependente"])
        st.dataframe(df_no_dep, use_container_width=True)
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

    st.subheader("Programadores sem Linguagens 📜")
    cursor.execute("""
        SELECT Nome_Programador, ID_Startup
        FROM programador
        WHERE ID_Startup IS NULL;
    """)
    result = cursor.fetchall()

    if result:
        df_no_lang = pd.DataFrame(
            result, columns=["Nome_Programador", "ID_Startup"])
        st.dataframe(df_no_lang, use_container_width=True)
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

    st.subheader("Linguagens sem Programadores ✖")
    cursor.execute("""
        SELECT Nome_Linguagem
        FROM linguagem AS l
        LEFT JOIN programador_linguagem AS pl ON l.ID_Linguagem = pl.ID_Linguagem
        WHERE ID_Programador IS NULL;
    """)
    result = cursor.fetchall()

    if result:
        df_no_prog = pd.DataFrame(result, columns=["Nome_Linguagem"])
        st.dataframe(df_no_prog, use_container_width=True)
    else:
        st.warning("Nenhum registro encontrado no banco de dados.")

else:
    st.error("Falha na conexão com o banco de dados.")
