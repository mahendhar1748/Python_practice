#Merging tables

import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")

cur1=con.cursor()

cur1.execute("create table empres as select * from emp2 union all select * from emp3")

cur1.execute("select * from empres")
for row in cur1:
    print(row)

cur1.close()

con.close()


