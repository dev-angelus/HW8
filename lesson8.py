import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e: #this error we need in all functions to catch errors
        print(e)

def create_student(conn, student):
    sql = '''INSERT INTO student(fullname, mark, hobby, is_married)
    VALUES(?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def read_student(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        for i in row:
            print(i)
    except Error as e:
        print(e)


database = "user.db"

sql_create_table = """
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
fullname VARCHAR(50) NOT NULL,
mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
is_married BOOLEAN DEFAULT FALSE
);
"""

connection = create_connection(database)

if connection is not None:
    print('All correct')
    # create_table(connection, sql_create_table)
    create_student(connection, ('Daniyar', 10.0, 'sleeping', True))
    read_student(connection)


# db = connection.cursor()
# db.execute("SELECT * FROM student")

# item = db.fetchall()
# for el in item:
#     print(el)