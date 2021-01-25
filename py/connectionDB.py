import sqlite3
import os


def updateDB(whichTable, nome, orario, url=''):
    try:
        sqliteConnection = sqlite3.connect('./manageDB/dbFiles/orari.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        if whichTable == 'chiuse':
                sqlite_insert_with_param = """INSERT INTO chiuse
                                (nome, url) 
                                VALUES (?, ?);"""
                data_tuple = ( nome, url)

        else:  # aperte
                sqlite_insert_with_param = """
                                INSERT INTO aperte
                                (nome, url, orario) 
                                VALUES (?, ?, ?);
                                """
                data_tuple = (nome, url, orario)
                
        
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

        #     cur.execute("insert into contacts (name, phone, email) values (?, ?, ?)",
        #     (name, phone, email))
