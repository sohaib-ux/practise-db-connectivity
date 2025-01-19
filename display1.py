import mysql.connector as c

mydb = c.connect(
    host=" 172.16.25.53",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()
mycursor.execute("select * from sunny order by score asc")
students=mycursor.fetchall()
for std in students:
    print(std)