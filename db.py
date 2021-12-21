import mysql.connector

mydb = mysql.connector.connect(host="localhost", auth_plugin='mysql_native_password',  user="test", passwd="test@123", database="mysaving")

mycursor = mydb.cursor()

mycursor.execute("select * from account")

for i in mycursor:
    print(i)



