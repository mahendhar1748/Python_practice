
#creating a table from another table

import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")

cur1=con.cursor()

cur1.execute("create table emp2 like emp1")

print("TABLE CREATED SUCCESSFULLY!!!")
#inserting data from one table to another table

cur1.execute("insert into emp2 select * from emp1")
print("DATA INSERTED SUCCESSFULLY!!!")

con.commit()

cur1.execute("select * from emp2")

for row in cur1:
    print(row)

cur1.close()
con.close()








    

