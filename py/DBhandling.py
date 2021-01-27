import sqlite3
import os



def updateDB(DBconnection, whichTable, nome, url='', orario=''):
    try:
        cursor = DBconnection.cursor()
        if whichTable == 'chiuse':
                sqlite_insert_with_param = """INSERT INTO chiuse
                                (nome, url) 
                                VALUES (?, ?);"""
                data_tuple = ( nome, url)

        elif whichTable == 'aperte':# aperte
                sqlite_insert_with_param = """
                                INSERT INTO aperte
                                (nome, url, orario) 
                                VALUES (?, ?, ?);
                                """
                data_tuple = (nome, url, orario)
                
        
        cursor.execute(sqlite_insert_with_param, data_tuple)
        DBconnection.commit()
        print("Python Variables inserted successfully into table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)

        

    

def emptyTables(DBconnection):
    cursor = DBconnection.cursor()
    cursor.execute("DELETE FROM aperte;")
    # sqliteConnection.commit()
    cursor.execute("DELETE FROM chiuse;")
    DBconnection.commit()
    cursor.execute("VACUUM;")
    cursor.close()