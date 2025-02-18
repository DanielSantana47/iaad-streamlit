import streamlit as st
from database import get_db_connection

st.title("🗑 Delete a Record")

id = st.number_input("Enter ID", min_value=1)

if st.button("Delete"):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM users WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        connection.commit()
        connection.close()
        st.success("Record Deleted Successfully!!!")
    else:
        st.error("Database connection failed")
