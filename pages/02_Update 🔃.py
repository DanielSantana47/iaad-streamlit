import streamlit as st
from database import get_db_connection

def get_records(query):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        connection.close()
        return {f"{r[1]} - {r[0]}": r[0] for r in records}
    return {}

def update_record(query, values):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        connection.close()
        st.success("Registro atualizado com sucesso!")
    else:
        st.error("Falha na conexão com o banco de dados")

def page_update_startup():
    st.title("Atualizar Startup 🔃")
    startups = get_records("SELECT ID_Startup, Nome_Startup FROM Startup")
    id_startup = st.selectbox("Startup", list(startups.keys()))
    nome = st.text_input("Novo Nome da Startup")
    cidade = st.text_input("Nova Cidade Sede")
    if st.button("Atualizar"):
        update_record("UPDATE Startup SET Nome_Startup=%s, Cidade_Sede=%s WHERE ID_Startup=%s", (nome, cidade, startups[id_startup]))

def page_update_programador():
    st.title("Atualizar Programador")
    programadores = get_records("SELECT ID_Programador, Nome_Programador FROM Programador")
    id_programador = st.selectbox("Programador", list(programadores.keys()))
    nome = st.text_input("Novo Nome do Programador")
    startups = get_records("SELECT ID_Startup, Nome_Startup FROM Startup")
    id_startup = st.selectbox("Nova Empresa", list(startups.keys()))
    genero = st.selectbox("Novo Gênero", ["M", "F"])
    data_nasc = st.date_input("Nova Data de Nascimento")
    if st.button("Atualizar"):
        update_record("UPDATE Programador SET Nome_Programador=%s, Genero_Programador=%s, Data_Nasc_Programador=%s, ID_Startup=%s WHERE ID_Programador=%s", (nome, genero, data_nasc, startups[id_startup], programadores[id_programador]))

def page_update_dependente():
    st.title("Atualizar Dependente")
    dependentes = get_records("SELECT ID_Dependente, Nome_Dependente FROM Dependente")
    id_dependente = st.selectbox("Dependente", list(dependentes.keys()))
    nome = st.text_input("Novo Nome do Dependente")
    parentesco = st.text_input("Novo Parentesco")
    data_nasc = st.date_input("Nova Data de Nascimento")
    if st.button("Atualizar"):
        update_record("UPDATE Dependente SET Nome_Dependente=%s, Parentesco_Dependente=%s, Data_Nasc_Dependente=%s WHERE ID_Dependente=%s", (nome, parentesco, data_nasc, dependentes[id_dependente]))

def page_update_linguagem():
    st.title("Atualizar Linguagem de Programação")
    linguagens = get_records("SELECT ID_Linguagem, Nome_Linguagem FROM Linguagem")
    id_linguagem = st.selectbox("Linguagem", list(linguagens.keys()))
    nome = st.text_input("Novo Nome da Linguagem")
    if st.button("Atualizar"):
        update_record("UPDATE Linguagem SET Nome_Linguagem=%s WHERE ID_Linguagem=%s", (nome, linguagens[id_linguagem]))

def page_update_programador_linguagem():
    st.title("Atualizar Programador x Linguagem")
    programadores = get_records("SELECT ID_Programador, Nome_Programador FROM Programador")
    id_programador = st.selectbox("Programador", list(programadores.keys()))
    linguagens = get_records("SELECT ID_Linguagem, Nome_Linguagem FROM Linguagem")
    id_linguagem = st.selectbox("Linguagem", list(linguagens.keys()))
    if st.button("Atualizar"):
        update_record("UPDATE Programador_Linguagem SET ID_Linguagem=%s WHERE ID_Programador=%s", (linguagens[id_linguagem], programadores[id_programador]))

# Sidebar para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Escolha uma página", ["Atualizar Startup", "Atualizar Programador", "Atualizar Dependente", "Atualizar Linguagem", "Atualizar Programador x Linguagem"])

if pagina == "Atualizar Startup":
    page_update_startup()
elif pagina == "Atualizar Programador":
    page_update_programador()
elif pagina == "Atualizar Dependente":
    page_update_dependente()
elif pagina == "Atualizar Linguagem":
    page_update_linguagem()
elif pagina == "Atualizar Programador x Linguagem":
    page_update_programador_linguagem()
