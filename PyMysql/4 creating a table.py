#creating a table in mysql(mydb19 database)

import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")
#here con is the connection object

#Creating cursor object
cur1=con.cursor()
cur1.execute("create table emp(eid int,ename varchar(20),sal int,sex varchar(1),dno int,city varchar(10))")
print("TABLE CREATED SUCCESSFULLY!!!")
cur1.close()
con.close()
#-------------------------------------------------------------------------------
#Goto database and check

mysql> use mydb19;
Database changed

mysql> show tables;
+------------------+
| Tables_in_mydb19 |
+------------------+
| emp              |
+------------------+
1 row in set (0.01 sec)

mysql> select * from emp;
Empty set (0.01 sec)
