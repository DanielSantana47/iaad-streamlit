import streamlit as st
from db import get_db_connection

st.title("➕ Create a Record")

name = st.text_input("Enter Name")
email = st.text_input("Enter Email")

if st.button("Create"):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO users(name, email) VALUES(%s, %s)"
        val = (name, email)
        cursor.execute(sql, val)
        connection.commit()
        connection.close()
        st.success("Record Created Successfully!!!")
    else:
        st.error("Database connection failed")
