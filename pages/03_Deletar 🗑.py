import streamlit as st
from database import get_db_connection

def get_records(query):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        connection.close()
        return {f"{r[0]} - {r[1]}": r[0] for r in records}
    return {}

def delete_record(query, values):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        if cursor.rowcount == 0:
            st.warning("O programador selecionado não possui relação com essa linguagem!")
        else:
            connection.commit()
            st.success("Registro deletado com sucesso!")
        connection.close()
    else:
        st.error("Falha na conexão com o banco de dados")

def page_delete_startup():
    st.title("Deletar Startup")
    startups = get_records("SELECT ID_Startup, Nome_Startup FROM Startup")
    id_startup = st.selectbox("Selecione a Startup para deletar", list(startups.keys()))
    if st.button("Deletar"):
        delete_record("DELETE FROM Startup WHERE ID_Startup=%s", (startups[id_startup],))

def page_delete_programador():
    st.title("Deletar Programador")
    programadores = get_records("SELECT ID_Programador, Nome_Programador FROM Programador")
    id_programador = st.selectbox("Selecione o Programador para deletar", list(programadores.keys()))
    if st.button("Deletar"):
        delete_record("DELETE FROM Programador WHERE ID_Programador=%s", (programadores[id_programador],))

def page_delete_dependente():
    st.title("Deletar Dependente")
    dependentes = get_records("SELECT ID_Dependente, Nome_Dependente FROM Dependente")
    id_dependente = st.selectbox("Selecione o Dependente para deletar", list(dependentes.keys()))
    if st.button("Deletar"):
        delete_record("DELETE FROM Dependente WHERE ID_Dependente=%s", (dependentes[id_dependente],))

def page_delete_linguagem():
    st.title("Deletar Linguagem de Programação")
    linguagens = get_records("SELECT ID_Linguagem, Nome_Linguagem FROM Linguagem")
    id_linguagem = st.selectbox("Selecione a Linguagem para deletar", list(linguagens.keys()))
    if st.button("Deletar"):
        delete_record("DELETE FROM Linguagem WHERE ID_Linguagem=%s", (linguagens[id_linguagem],))

def page_delete_programador_linguagem():
    st.title("Deletar Programador x Linguagem")
    programadores = get_records("SELECT ID_Programador, Nome_Programador FROM Programador")
    id_programador = st.selectbox("Selecione o Programador", list(programadores.keys()))
    linguagens = get_records("SELECT ID_Linguagem, Nome_Linguagem FROM Linguagem")
    id_linguagem = st.selectbox("Selecione a Linguagem", list(linguagens.keys()))
    if st.button("Deletar"):
        delete_record("DELETE FROM Programador_Linguagem WHERE ID_Programador=%s AND ID_Linguagem=%s", (programadores[id_programador], linguagens[id_linguagem]))

# Sidebar para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Escolha uma página", ["Deletar Startup", "Deletar Programador", "Deletar Dependente", "Deletar Linguagem", "Deletar Programador x Linguagem"])

if pagina == "Deletar Startup":
    page_delete_startup()
elif pagina == "Deletar Programador":
    page_delete_programador()
elif pagina == "Deletar Dependente":
    page_delete_dependente()
elif pagina == "Deletar Linguagem":
    page_delete_linguagem()
elif pagina == "Deletar Programador x Linguagem":
    page_delete_programador_linguagem()
