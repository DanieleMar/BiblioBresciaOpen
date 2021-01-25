import sqlite3, os

def connectDB():
        conn = sqlite3.connect('./manageDB/dbFiles/orari.db')



        c = conn.cursor()

        # Create table
        # c.execute('''CREATE TABLE open
        #              (nome text, orario text, url text)''')

        # c.execute('''CREATE TABLE chiuse
        #             (nome text, orario text, url text)
        # ''')

        c.execute('''CREATE TABLE assenti
                (nome text)
        ''')

        # Insert a row of data
        # c.execute("INSERT INTO open VALUES (,'BUY','RHAT',100,35.14)")

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()