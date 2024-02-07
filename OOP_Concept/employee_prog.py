class emp:
    company="Broadridge"
    def getdetails(self):
        self.ename=input("enter the name of employee: ")
        self.eid=int(input("enter the id-no of an employee: "))
        self.esalary=int(input("enter the salary of an employee"))
    def putdetails(self):
        print("employee name:",self.ename)
        print("employee id :",self.eid)
        print("employee salary:",self.esalary)
e1=emp()
e1.getdetails()
e1.putdetails()
e2=emp()
e2.getdetails()
e2.putdetails()
e1.esalary=e1.esalary-10000
print(e1.esalary)
e3=emp()
e3.getdetails()
e3.putdetails()
        
                     
