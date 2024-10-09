
#SQL - Structured-Query-Language

#It is a language which is followed by all the databases

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| digitalnest        |
| djangodb1          |
| djangodb2          |
| djangodb3          |
| djangodb4          |
| information_schema |
| mydb1              |
| mydb10             |
| mydb11             |
| mydb12             |
| mydb13             |
| mydb14             |
| mydb15             |
----------------------

mysql> create database mydb18;

mysql> use mydb18;

mysql> show tables;

#CRUD Operations
C - CREATE
R - READ
U - UPDATE
D - DELETE

#1) Creating a table in database

mysql> create table student(name varchar(20),rollno int,marks int);

#2)Inserting data into the table

mysql> insert into student values('Miller',501,90);

mysql> insert into student values('Blake',502,80),('James',503,70),('Rahul',504,60);

#3) Retrieving data from the table using select stmt.

#i) Retrieving all the columns

mysql> select * from student;
+--------+--------+-------+
| name   | rollno | marks |
+--------+--------+-------+
| Miller |    501 |    90 |
| Blake  |    502 |    80 |
| James  |    503 |    70 |
| Rahul  |    504 |    60 |
+--------+--------+-------+

#ii) Retrieving specific columns
mysql> select name,marks from student;
+--------+-------+
| name   | marks |
+--------+-------+
| Miller |    90 |
| Blake  |    80 |
| James  |    70 |
| Rahul  |    60 |
+--------+-------+

#---------------------------------------------------------------------------------------------
#2. creating emp table

mysql> create table emp(eid int,ename varchar(10),sal int,sex varchar(1),dno int,city varchar(10));

#inserting data

mysql> insert into emp values(101,'Miller',10000,'m',11,'hyd'),(102,'Blake',20000,'m',12,'pune'),
(103,'sony',30000,'f',11,'pune'),(104,'Sonia',40000,'f',12,'hyd'),
(105,'James',50000,'m',13,'hyd');

#Retrieving data
mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 20000 | m    |   12 | pune |
|  103 | sony   | 30000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+

#mysql> select ename,sal from emp;
+--------+-------+
| ename  | sal   |
+--------+-------+
| Miller | 10000 |
| Blake  | 20000 |
| sony   | 30000 |
| Sonia  | 40000 |
| James  | 50000 |
+--------+-------+

#------------------------------------------------------------------------------------------
#4) Filtering operations:

#i) I want only empname "Blake" record

mysql> select * from emp where ename="Blake";
+------+-------+-------+------+------+------+
| eid  | ename | sal   | sex  | dno  | city |
+------+-------+-------+------+------+------+
|  102 | Blake | 20000 | m    |   12 | pune |
+------+-------+-------+------+------+------+

#ii) I want only those emps who belongs to the dno 11.

mysql> select * from emp where dno=11;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  103 | sony   | 30000 | f    |   11 | pune |
+------+--------+-------+------+------+------+


#iii) I want only those emps who belongs to the city "hyd"

mysql> select * from emp where city='hyd';
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+

#providing multiple conditions
#iv) Filter those emps whose salaries are above 20000 and belongs to dno=12

mysql> select * from emp where sal>20000 and dno=12;
+------+-------+-------+------+------+------+
| eid  | ename | sal   | sex  | dno  | city |
+------+-------+-------+------+------+------+
|  104 | Sonia | 40000 | f    |   12 | hyd  |
+------+-------+-------+------+------+------+

#----------------------------------------------------------------------------------------------
mysql> show tables;
+------------------+
| Tables_in_mydb18 |
+------------------+
| emp              |
| student          |
+------------------+
#---------------------------------------------------------------------------------------------

#5)update:

mysql> update emp set sal=sal+5000 where ename="Blake";

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 30000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+

#ii)incrementing the salaries of dno 11 employees with 7000/-
mysql> update emp set sal=sal+7000 where dno=11;

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 17000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 37000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
|  105 | James  | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+

#modifying the name "James" to "John"

mysql> update emp set ename="John" where eid=105;

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 17000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 37000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
|  105 | John   | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+

#--------------------------------------------------------------------------------
#6)Delete:
#ex: Delete the record of "John"

mysql> delete from emp where eid=105;

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 17000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 37000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
-----------------------------------------------

#ii)delete  from emp where dno=11; ----->all dno 11 records will be deleted
#iii)delete from emp where city="pune"->all pune records will be deleted
#iv)delete from emp where city!="hyd";->except hyd records all other records are deleted

#here for deleting,we can use all the comparision operators-> > , < ,>= , <= ,==,!=

#---------------------------------------------------------------------------------

#Groupings and aggregations:
#Various Aggregations -------->sum(),max(),min(),avg(),count()
1.Single Grouping and Single Aggregation

#o/p
males totsal
females tosal

mysql> select sex,sum(sal) from emp group by sex;
+------+----------+
| sex  | sum(sal) |
+------+----------+
| m    |    42000 |
| f    |    77000 |
+------+----------+
#ii) dno wise---->total salaries
mysql> select dno,sum(sal) from emp group by dno;
+------+----------+
| dno  | sum(sal) |
+------+----------+
|   11 |    54000 |
|   12 |    65000 |
+------+----------+

#iii)city wise----->total salaries.
mysql> select city,sum(sal) from emp group by city;
+------+----------+
| city | sum(sal) |
+------+----------+
| hyd  |    57000 |
| pune |    62000 |
+------+----------+

#2) Multi grouping and single Aggregation

dno wise,sex wise---->totsal]

11 m--->totsal
   f--->totsal

12 m --->totsal
   f --->totsal

mysql> select dno,sex,sum(sal) from emp group by dno,sex;
+------+------+----------+
| dno  | sex  | sum(sal) |
+------+------+----------+
|   11 | m    |    17000 |
|   12 | m    |    25000 |
|   11 | f    |    37000 |
|   12 | f    |    40000 |
+------+------+----------+
#3)single grouping and multiple aggregation

mysql> select dno,sum(sal),avg(sal),max(sal),min(sal),count(*) from emp group by dno;
+------+----------+------------+----------+----------+----------+
| dno  | sum(sal) | avg(sal)   | max(sal) | min(sal) | count(*) |
+------+----------+------------+----------+----------+----------+
|   11 |    54000 | 27000.0000 |    37000 |    17000 |        2 |
|   12 |    65000 | 32500.0000 |    40000 |    25000 |        2 |
+------+----------+------------+----------+----------+----------+

#4)multi grouping and multiple aggregation:
#o/p:
11 m  totsal avgsal maxsal minsal count
   f  totsal   "      "       "     "

12 m totsal
   f totsal

13 m totsal
   f totsal


mysql> select dno,sex,sum(sal),avg(sal),max(sal),min(sal),count(sal) from emp group by dno,sex;
+------+------+----------+------------+----------+----------+------------+
| dno  | sex  | sum(sal) | avg(sal)   | max(sal) | min(sal) | count(sal) |
+------+------+----------+------------+----------+----------+------------+
|   11 | m    |    17000 | 17000.0000 |    17000 |    17000 |          1 |
|   12 | m    |    25000 | 25000.0000 |    25000 |    25000 |          1 |
|   11 | f    |    37000 | 37000.0000 |    37000 |    37000 |          1 |
|   12 | f    |    40000 | 40000.0000 |    40000 |    40000 |          1 |
+------+------+----------+------------+----------+----------+------------+

#---------------------------------------------------------------------------------------------
#8. creating a table from another table

mysql> create table emp2 like emp;

#here only the table structure is created, we wont get the data

mysql> show tables;
+------------------+
| Tables_in_mydb18 |
+------------------+
| emp              |
| emp2             |
| student          |
+------------------+
3 rows in set (0.00 sec)

mysql> select * from emp2;
Empty set (0.00 sec)

#inserting data from one table to another table
#inserting data from emp to emp2
mysql> insert into emp2 select * from emp;

mysql> select * from emp2;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 17000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 37000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#---------------------------------------------------------------------------------------------
#9. table to table copy (CTAS)--->CREATE -TABLE -As -SELECT

mysql> create table emp3 as select * from emp;

mysql> select * from emp3;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 17000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 37000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#--------------------------------------------------------------------------------------------
#10. merging 2 tables

mysql> create table empres select * from emp2 union all select * from emp3;

mysql> select * from empres;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 17000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 37000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
|  101 | Miller | 17000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | sony   | 37000 | f    |   11 | pune |
|  104 | Sonia  | 40000 | f    |   12 | hyd  |
+------+--------+-------+------+------+------+

#---------------------------------------------------------------------------------------------
#11.eliminating the duplicates:


mysql> create table empres2 select distinct(eid),ename,sal,sex,dno from empres;
Query OK, 4 rows affected (0.06 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from empres2;
+------+--------+-------+------+------+
| eid  | ename  | sal   | sex  | dno  |
+------+--------+-------+------+------+
|  101 | Miller | 17000 | m    |   11 |
|  102 | Blake  | 25000 | m    |   12 |
|  103 | sony   | 37000 | f    |   11 |
|  104 | Sonia  | 40000 | f    |   12 |
+------+--------+-------+------+------+

#---------------------------------------------------------------------------------------------
#12. Alter:

#i)Adding new columns------->dname and designation

mysql> alter table emp2
    -> add dname varchar(10),
    -> add designation varchar(10);
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from emp2;
+------+--------+-------+------+------+------+-------+-------------+
| eid  | ename  | sal   | sex  | dno  | city | dname | designation |
+------+--------+-------+------+------+------+-------+-------------+
|  101 | Miller | 17000 | m    |   11 | hyd  | NULL  | NULL        |
|  102 | Blake  | 25000 | m    |   12 | pune | NULL  | NULL        |
|  103 | sony   | 37000 | f    |   11 | pune | NULL  | NULL        |
|  104 | Sonia  | 40000 | f    |   12 | hyd  | NULL  | NULL        |
+------+--------+-------+------+------+------+-------+-------------+

#--------------------------------------------------------------------------------------------
#ii)Renaming a column using alter command
#Rename  sex---->Gender
#        sal---->income

mysql> alter table emp2
    -> change column sex Gender varchar(10),
    -> change column sal income int;

mysql> select * from emp2;
+------+--------+--------+--------+------+------+-------+-------------+
| eid  | ename  | income | Gender | dno  | city | dname | designation |
+------+--------+--------+--------+------+------+-------+-------------+
|  101 | Miller |  17000 | m      |   11 | hyd  | NULL  | NULL        |
|  102 | Blake  |  25000 | m      |   12 | pune | NULL  | NULL        |
|  103 | sony   |  37000 | f      |   11 | pune | NULL  | NULL        |
|  104 | Sonia  |  40000 | f      |   12 | hyd  | NULL  | NULL        |
+------+--------+--------+--------+------+------+-------+-------------+

#-------------------------------------------------------------------------------------------
#iii) dropping a particular column

mysql> alter table emp2
    -> drop column dname;

mysql> select * from emp2;
+------+--------+--------+--------+------+------+-------------+
| eid  | ename  | income | Gender | dno  | city | designation |
+------+--------+--------+--------+------+------+-------------+
|  101 | Miller |  17000 | m      |   11 | hyd  | NULL        |
|  102 | Blake  |  25000 | m      |   12 | pune | NULL        |
|  103 | sony   |  37000 | f      |   11 | pune | NULL        |
|  104 | Sonia  |  40000 | f      |   12 | hyd  | NULL        |
+------+--------+--------+--------+------+------+-------------+

#---------------------------------------------------------------------------------------------
#iv) Renaming a table:

mysql> alter table emp2
    -> rename to emps;

mysql> select * from emp2;
ERROR 1146 (42S02): Table 'mydb18.emp2' doesn't exist
mysql> select * from emps;
+------+--------+--------+--------+------+------+-------------+
| eid  | ename  | income | Gender | dno  | city | designation |
+------+--------+--------+--------+------+------+-------------+
|  101 | Miller |  17000 | m      |   11 | hyd  | NULL        |
|  102 | Blake  |  25000 | m      |   12 | pune | NULL        |
|  103 | sony   |  37000 | f      |   11 | pune | NULL        |
|  104 | Sonia  |  40000 | f      |   12 | hyd  | NULL        |
+------+--------+--------+--------+------+------+-------------+

#----------------------------------------------------------------------------------------------
#drop :for droping the entire table

mysql> drop table emp3;

mysql> select * from emp3;
ERROR 1146 (42S02): Table 'mydb18.emp3' doesn't exist

#----------------------------------------------------------------------------------------------




































































































































