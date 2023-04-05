import mysql.connector
from mysql.connector import Error



def createConnection():
    connection = None
    try:
        connection = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="1111")
        print ("Connection OK")
    except Error as e:
        print(f"Ошибка {e}")
    return connection

def createDatabase(db: mysql.connector):
    cursor = db.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS notes")
        print("CreateDatabase OK")
    except Error as e:
        print(f"Ошибка {e}")

def createTable(db:mysql.connector):
    cursor = db.cursor()
    createDatabase(db)
    db.database = "notes"
    try:
        zapros = "CREATE TABLE IF NOT EXISTS noteTable (" \
                "ID  INT AUTO_INCREMENT PRIMARY KEY, " \
                "title VARCHAR(255) NOT NULL, " \
                "note VARCHAR(2000) NOT NULL)"
        cursor.execute(zapros)
        print("CreateTable: OK")
    except Error as e:
        print(f"Ошибка {e}")


def insertNote(db:mysql.connector, title, note):
    db.database = "notes"
    cursor = db.cursor()

    zapros = "INSERT INTO noteTable (title, note) VALUES (%s, %s)"
    value = (title, note)
    cursor.execute(zapros, value)
    db.commit()
    return cursor.lastrowid

def selectAllNotes(db:mysql.connector):
    db.database = "notes"
    query = "SELECT * from noteTable"
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def selectSpecificNote(db:mysql.connector, note_id):
    db.database = "notes"
    cursor = db.cursor()
    cursor.execute("SELECT title, note FROM noteTable WHERE ID = " + str(note_id))
    return cursor.fetchone()

def updateNote(db:mysql.connector, title, note, noteId):
    db.database = "notes"
    cursor = db.cursor()
    zapros = "UPDATE noteTable SET title = %s, note = %s WHERE ID = %s"
    value = [title, note, noteId]
    cursor.execute(zapros, value)
    db.commit()

def deleteNote(db:mysql.connector, noteId):
    db.database = "notes"
    cursor = db.cursor()
    zapros = "DELETE FROM notesTable WHERE ID = %s"
    adr = (noteId,)
    cursor.execute(zapros, adr)
    db.commit()

def deleteDatabase(db:mysql.connector):
    cursor = db.cursor()
    cursor.execute("DROP DATABASE notes")

