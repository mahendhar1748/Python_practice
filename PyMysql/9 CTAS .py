
#CTAS :CREATE-TABLE-AS-SELECT
#Creating a table from another table

import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="mydb19")

cur1=con.cursor()

cur1.execute("CREATE TABLE EMP3 AS SELECT * FROM EMP")

cur1.execute("select * from emp3")

for row in cur1:
    print(row)
cur1.close()
con.close()






















