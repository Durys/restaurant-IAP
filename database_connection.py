import pyodbc
import pandas as pd
import sqlite3


def get_data_from_database(server, database, username, password):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                          ';DATABASE=' + database +
                          ';UID=' + username +
                          ';PWD=' + password)
    sql = "SELECT * FROM database_name.table"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = pd.read_sql(sql, conn)

    return data


def get_from_db_file(df_file_path=None):
    df_file_path = "Data\\restaurant.db"
    con = sqlite3.connect(df_file_path)

    cur = con.cursor()

    table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
    correct_tables = []
    dfs = []

    for i in table_list:
        stri = ''.join(i)
        correct_tables.append(stri)

    for table in correct_tables:
        sql = "SELECT * FROM " + table
        df = pd.read_sql_query(sql, con)
        dfs.append(df)

    con.close()

    return dfs[1:]

