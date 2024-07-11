import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pwd",
    database="student_db"
)

cursorObject = database.cursor()

studentRecord = """CREATE TABLE STUDENT (
                NAME VARCHAR(50) NOT NULL,
                BRANCH VARCHAR(50),
                ROLL INT NOT NULL,
                SECTION VARCHAR(10),
                AGE INT
                )"""

cursorObject.execute(studentRecord)

database.close()

