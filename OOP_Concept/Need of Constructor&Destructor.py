# Need of constructor and Destructor.

class employee:
    empcount=0

    def __init__(self,x,y):
        self.ename=x
        self.eid=y
        employee.empcount+=1

    def __del__(self):
        print("Destuctor executes ")
        employee.empcount-=1

    def display(self):
        print("employe Name -:",self.ename,"& ", "employee ID -:",self.eid)

emp1=employee("mahendhar",143)
emp2=employee("Laxman",1)
emp1.display()
emp2.display()
print("total no of employees :-",employee.empcount)
del emp1
del emp2
print("total no of employees :-",employee.empcount)
