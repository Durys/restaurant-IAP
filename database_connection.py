import pyodbc
import pandas as pd
import sqlite3


def get_data_from_database(server, database, username, password):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server +
                          ';DATABASE=' + database +
                          ';UID=' + username +
                          ';PWD=' + password)
    sql = 'SELECT * FROM database_name.table'
    cursor = conn.cursor()
    cursor.execute(sql)
    data = pd.read_sql(sql, conn)

    return data


def get_from_db_file(df_file_path):
    df_file_path = "Data\\restaurant.db"
    conn = sqlite3.connect(df_file_path)

    cursor = conn.cursor()

    table_list = [a for a in cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
    print(table_list)

    sql = 'SELECT * FROM database_name.table'
    cursor.execute(sql)
    data = pd.read_sql(sql, conn)

    return data

