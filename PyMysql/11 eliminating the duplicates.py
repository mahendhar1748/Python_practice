
#Removing the duplicates

import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")

cur1=con.cursor()

cur1.execute("create table empres2 as select distinct(eid),ename,sal,sex,dno,city from empres")

cur1.execute("select * from empres2")
for row in cur1:
    print(row)

cur1.close()

con.close()


