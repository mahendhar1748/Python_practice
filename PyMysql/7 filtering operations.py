#Filtering operations:

import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")

#Creating cur1 object for creating table
cur1=con.cursor()

#1.filter only the employees belonging to city hyd
cur1.execute("select * from emp where city='hyd'")

for row in cur1:
    print(row)
print("\n")
#2.filter those whose sal>20000 and dno is 12
cur1.execute("select * from emp where sal>20000 and dno=12")

for row in cur1:
    print(row)

print("\n")
#----------------------------------------------------------------------------------------------
#Bydefault we get the o/p records in tuple format,but I want records in lists
    
cur1.execute("select * from emp")

for row in cur1:
    print(list(row))
print("\n")
#---------------------------------------------------------------------------------------------
#Now storing all the retrieved records within a list
x=[]

cur1.execute("select * from emp")
for row in cur1:
    x.append(list(row))
print(x)
print("\n")
x[4][2]=60000
print(x)
cur1.close()
con.close()















