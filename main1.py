import mysql.connector as c

mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS sunny (id INT PRIMARY KEY,name VARCHAR(100),city VARCHAR(100),score INT)")

mydb.commit()

print("Table 'student' created successfully")

mycursor.close()
mydb.close()
