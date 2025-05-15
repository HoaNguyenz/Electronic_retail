import pymssql

def get_db_connection():
    conn = pymssql.connect(
        server='localhost',
        user='sa',
        password='hungle123@@',
        database='E_Retail'
    )
    return conn
