import sqlite3

def isTableExists(conn_name, db_name):
    connection = sqlite3.connect(conn_name)
    cur = connection.cursor()
    cur.execute('SELECT NAME FROM sqlite_master WHERE TYPE="table" AND name = :id', {"id": db_name})
    qd = cur.fetchone()
    connection.close()
    if qd is not None:
        return True
    else:
        return False


