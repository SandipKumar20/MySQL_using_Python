import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pwd",
    database="student_db"
)

cursorObject = database.cursor()

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"

val = [("Govind", "CSE", "98", "A", "18"),
       ("Kalyani", "CSE", "99", "A", "18"),
       ("Appu", "MAE", "43", "B", "20"),
       ("Kumari", "ECE", "24", "A", "21"),
       ("Kumar", "MAE", "45", "B", "20"),
       ("Vasantha", "ECE", "55", "A", "22")]

cursorObject.executemany(sql, val)
database.commit()

database.close()