import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pwd",
    database="student_db"
)

cursorObject = database.cursor()

query = "UPDATE STUDENT SET AGE = 23 WHERE NAME = 'Ram'"
cursorObject.execute(query)
database.commit()
database.close()