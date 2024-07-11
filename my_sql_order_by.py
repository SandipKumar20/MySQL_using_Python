import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pwd",
    database="student_db"
)

cursorObject = database.cursor()

query = "SELECT * FROM STUDENT ORDER BY NAME DESC"
cursorObject.execute(query)

results = cursorObject.fetchall()

for x in results:
    print(x)

database.close()