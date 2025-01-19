import mysql.connector as c
 
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)
 
mycursor = mydb.cursor()
id = input("Enter the id of the student to update: ")
new_name = input("Enter the new name: ")
mycursor.execute("UPDATE student3 SET sname = %s WHERE sid = %s", (new_name, id))
mydb.commit()
print("updated successfully")