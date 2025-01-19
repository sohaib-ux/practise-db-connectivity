import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE student3 (sid INT, sname VARCHAR(20))")
print("table created")

