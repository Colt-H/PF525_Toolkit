import sqlite3
import os
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as return_error:
        print(return_error)

    return conn

def update_parameter_notes(conn, update):
    try:
        sql = ''' UPDATE param_xref
                  SET Notes = ?
                  WHERE PF40_Param = ? COLLATE NOCASE'''
        cur = conn.cursor()
        cur.execute(sql, update)
        conn.commit()
    except Error as update_error:
        print(update_error)

def update_main():
    while True:
        database = os.path.abspath('./PF525_Toolkit/Database/param_xref.db')

        conn = create_connection(database)
        with conn:
            parameter = input("Enter the PF40 Parameter Number or (Q) to go back: ")
            note = input("Enter the new note: ")
            if parameter == ('q' or 'Q'):
                break
            else:
                update = (note, parameter)
                update_parameter_notes(conn, update)


if __name__ == '__main__':
    update_main()
