#program student
class student:
    def __init__(self):
        self.sname=input("enter the value of Student Name")
        self.sid=int(input("enter the id of student"))
        self.sbranch=(input("enter student branch: "))
        self.rank=int(input("enter the rank: "))
    def display(self):
        print("student Name: ",self.sname)
        print("student id: ",self.sid)
        print("student branch: ",self.sbranch)
        print("student rank: ",self.rank)
print("student details")
s1=student()
s1.display
s2=student()
s2.display()
print(s1.sname)
