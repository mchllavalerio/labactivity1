import streamlit as st
import pyodbc
import pandas as pd

def create_connection():
    server = 'DESKTOP-34LMCM7\SQLEXPRESS'
    database = 'TMI'
    username = ''
    password = ''
    driver = '{ODBC Driver 18 for SQL Server}'
    
    conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};TrustServerCertificate=yes;trusted_connection=True;'
    conn = pyodbc.connect(conn_str)
    return conn

def main():
    st.title('SQL Server Connection Example')

    try:
        conn = create_connection()
        st.success("Connected to the database successfully!")
    except Exception as e:
        st.error(f"Failed to connect to the database: {e}")
        return

    query = "SELECT * FROM ACCOUNT"
    
    try:
        df = pd.read_sql(query, conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Failed to execute query: {e}")

    conn.close()

if __name__ == '__main__':
    main()
