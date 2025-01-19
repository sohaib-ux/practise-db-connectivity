import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()
id=int(input("enter the student id to delete:"))
mycursor.execute("delete from sunny where id=%s",(id))
print(f" record with id {id}  deleted successfully")
mydb.commit()