import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()
#id=input("enter the id:")
#name=input("enter your name")
mycursor.execute("INSERT INTO student3 values (200,'sunny')")
print("inserted successfully")
mydb.commit()

