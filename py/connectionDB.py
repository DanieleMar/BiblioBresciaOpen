import sqlite3, os

def updateDB(nome, url):
    try:
        sqliteConnection = sqlite3.connect('./manageDB/dbFiles/orari.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO chiuse
                          (nome, url) 
                          VALUES (?, ?);"""

        data_tuple = (nome, url)
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