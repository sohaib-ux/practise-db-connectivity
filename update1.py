import mysql.connector as c
 
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)
 
mycursor = mydb.cursor()
id=int(input("Enter the student id to update:"))
updated_name=input("Enter the  updated name: ")
mycursor.execute("update sunny  set name=%s where id=%s",(updated_name,id))
mydb.commit()
print("record updated successfully")
 