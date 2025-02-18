import streamlit as st
from database import get_db_connection

st.title("✏️ Update a Record")

id = st.number_input("Enter ID", min_value=1)
name = st.text_input("Enter New Name")
email = st.text_input("Enter New Email")

if st.button("Update"):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
        val = (name, email, id)
        cursor.execute(sql, val)
        connection.commit()
        connection.close()
        st.success("Record Updated Successfully!!!")
    else:
        st.error("Database connection failed")
