#Creating multiple cursor objects

#cur1----->for creating table
#cur2----->for inserting data
#cur3----->for retrieving data
import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")

#Creating cur1 object for creating table
cur1=con.cursor()
cur1.execute("create table emp1(eid int,ename varchar(10),sal int,sex varchar(1),dno int,city varchar(10))")

#Creating cur2 object for inserting data
cur2=con.cursor()
cur2.execute("insert into emp1 values(101,'Miller',10000,'m',11,'hyd'),(102,'Blake',20000,'m',12,'pune'),(103,'sony',30000,'f',11,'pune'),(104,'Sonia',40000,'f',12,'hyd'),(105,'James',50000,'m',13,'hyd')")
con.commit()

#Creating cur3 object for retrieving data
cur3=con.cursor()
cur3.execute("select * from emp1")

for row in cur3:
    print(row)

cur1.close()
cur2.close()
cur3.close()
con.close()

#Note: we can perform all the above operations using single cursor object also

#when to go for multiple cursor objects

#ex: cur1.execute("select * from emp") --->here emp1 records are stored in cur1 object
#ex: cur1.execute("select * from customer")--->here now customer records are stored in cur1

#so for retrieving 2 tables data-->create 2 cursor objects













