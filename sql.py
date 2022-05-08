import mysql.connector

#establishing connection with database
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="registration"
)

#preparing cursor object
mycursor=db.cursor()

#creating database
#mycursor.execute("CREATE DATABASE registration")

#creating table
new_table ="CREATE TABLE userdata(f_name VARCHAR(30),s_name VARCHAR(30),gender VARCHAR(8),age INT(4),addr VARCHAR(60),city VARCHAR(25),stat VARCHAR(20),phone VARCHAR(16),email VARCHAR(30),username VARCHAR(30),pass VARCHAR(40),imglink VARCHAR(80),img_collect VARCHAR(200))"
#mycursor.execute(new_table)

#inserting values to a database
'''sql = "INSERT INTO userdata(uname,password)VALUES(%s,%s)"
val = ("Neeraj","hello")
mycursor.execute(sql,val)
db.commit()'''

#printing stored values in database
mycursor.execute("SELECT * FROM userdata")
myresult= mycursor.fetchall()
for x in myresult:
    print(x)
