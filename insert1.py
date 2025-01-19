import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()
num_records=int(input("enter the no of records you want to insert:"))
for _ in range(num_records):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    city = input("Enter student city: ")
    score = input("Enter student score: ")

    mycursor.execute("INSERT INTO sunny (id, name, city, score) VALUES (%s, %s, %s, %s)", (id, name, city, score))

mydb.commit()

print(f"{num_records} records inserted successfully")





mycursor.close()
mydb.close()
