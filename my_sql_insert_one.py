import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pwd",
    database="student_db"
)

cursorObject = database.cursor()

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"
val = ("Tom", "CSE", "85", "B", "19")

cursorObject.execute(sql, val)
database.commit()

database.close()