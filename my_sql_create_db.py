import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pwd",
    )

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE student_db")