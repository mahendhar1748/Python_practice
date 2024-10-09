
#python program to create a database in mysql

import pymysql

#Now creating connection object-->to connect with database
#if we call connect() function by providing connecting parameters , then connection
# object is created
#connection parameters such as
#1.host
#2.username of database
#3.password of database
#4.databasename
con=pymysql.connect(host='localhost',user='root',password='root')
#here con is the connection object(we can provide any name)

#Next creating cursor object
#if we pass cursor() method on connection object, cursor object is created.

cur1=con.cursor() #here cur1 is the cursor object

#within the cursor object(cur1), we have execute method, within which we can
#specify any valid sql query
cur1.execute("create database mydb19")

print("DATABASE CREATED SUCCESSFULLY!!!")

cur1.close()

con.close()















