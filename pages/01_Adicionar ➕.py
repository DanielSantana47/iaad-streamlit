import streamlit as st
from database import get_db_connection

def get_startups():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID_Startup, Nome_Startup FROM Startup")
        startups = cursor.fetchall()
        connection.close()
        return {f"{nome} (ID: {id_})": id_ for id_, nome in startups}
    return {}

def get_programadores():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID_Programador, Nome_Programador FROM Programador")
        programadores = cursor.fetchall()
        connection.close()
        return {f"{nome} (ID: {id_})": id_ for id_, nome in programadores}
    return {}

def get_linguagens():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT ID_Linguagem, Nome_Linguagem FROM Linguagem")
        linguagens = cursor.fetchall()
        connection.close()
        return {f"{nome} (ID: {id_})": id_ for id_, nome in linguagens}
    return {}

def insert_record(query, values):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()
        connection.close()
        st.success("Registro criado com sucesso!")
    else:
        st.error("Falha na conexão com o banco de dados")

def page_startup():
    st.title("Adicionar Startup")
    nome = st.text_input("Nome da Startup")
    cidade = st.text_input("Cidade Sede")
    if st.button("Adicionar"):
        insert_record("INSERT INTO Startup (Nome_Startup, Cidade_Sede) VALUES (%s, %s)", (nome, cidade))

def page_programador():
    st.title("Adicionar Programador")
    nome = st.text_input("Nome do Programador")
    genero = st.selectbox("Gênero", ["M", "F"])
    data_nasc = st.date_input("Data de Nascimento")
    startups = get_startups()
    startup_nome = st.selectbox("Startup", list(startups.keys()))
    id_startup = startups[startup_nome] if startup_nome else None
    if st.button("Adicionar"):
        insert_record("INSERT INTO Programador (Nome_Programador, Genero_Programador, Data_Nasc_Programador, ID_Startup) VALUES (%s, %s, %s, %s)", (nome, genero, data_nasc, id_startup))

def page_dependente():
    st.title("Adicionar Dependente")
    nome = st.text_input("Nome do Dependente")
    parentesco = st.text_input("Parentesco")
    data_nasc = st.date_input("Data de Nascimento")
    programadores = get_programadores()
    programador_nome = st.selectbox("Programador Responsável", list(programadores.keys()))
    id_responsavel = programadores[programador_nome] if programador_nome else None
    if st.button("Adicionar"):
        insert_record("INSERT INTO Dependente (Nome_Dependente, Parentesco_Dependente, Data_Nasc_Dependente, ID_Responsavel) VALUES (%s, %s, %s, %s)", (nome, parentesco, data_nasc, id_responsavel))

def page_linguagem():
    st.title("Adicionar Linguagem de Programação")
    nome = st.text_input("Nome da Linguagem")
    if st.button("Adicionar"):
        insert_record("INSERT INTO Linguagem (Nome_Linguagem) VALUES (%s)", (nome,))

def page_programador_linguagem():
    st.title("Associar Programador a Linguagem")
    programadores = get_programadores()
    programador_nome = st.selectbox("Programador", list(programadores.keys()))
    id_programador = programadores[programador_nome] if programador_nome else None
    
    linguagens = get_linguagens()
    linguagem_nome = st.selectbox("Linguagem", list(linguagens.keys()))
    id_linguagem = linguagens[linguagem_nome] if linguagem_nome else None
    
    if st.button("Associar"):
        insert_record("INSERT INTO Programador_Linguagem (ID_Programador, ID_Linguagem) VALUES (%s, %s)", (id_programador, id_linguagem))

# Sidebar para navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Escolha uma página", ["Startup", "Programador", "Dependente", "Linguagem", "Programador x Linguagem"])

if pagina == "Startup":
    page_startup()
elif pagina == "Programador":
    page_programador()
elif pagina == "Dependente":
    page_dependente()
elif pagina == "Linguagem":
    page_linguagem()
elif pagina == "Programador x Linguagem":
    page_programador_linguagem()