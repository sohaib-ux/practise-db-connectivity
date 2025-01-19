import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()
mycursor.execute("select * from student3")
students=mycursor.fetchall();
for std in students:
    print(std)