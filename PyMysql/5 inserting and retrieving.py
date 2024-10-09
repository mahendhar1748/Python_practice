#Python program to insert data into a table and retrieving the records

import pymysql

#creating connection object(con)
con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")

#Creating cursor object(cur1)
cur1=con.cursor()

cur1.execute("insert into emp values(101,'Miller',10000,'m',11,'hyd'),(102,'Blake',20000,'m',12,'pune'),(103,'sony',30000,'f',11,'pune'),(104,'Sonia',40000,'f',12,'hyd'),(105,'James',50000,'m',13,'hyd')")
con.commit()  #for permanently saving
print("Data Inserted Successfully!!!")

#Now retrieving the data
cur1.execute("select * from emp")
#The o/p records from the sql query(Select) are stored within cur1 object

#use for loop and get one by one record.

for row in cur1:
    print(row)

cur1.close()
con.close()








