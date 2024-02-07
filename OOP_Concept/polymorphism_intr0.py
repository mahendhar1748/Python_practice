#--------POLYMORPHISM------------------------------------
'''
poly====>many forms
ability to take morethan one input

-- the concept of defining many methods with same name and same arguments
or functionalities to solve particular problem is nothing but polymorphism
--there are mainly two typs
1.static polymorphism -(method overloading)
2.Dynamic polymorphism -(method overriding)

*But python supports only method overriding(Dymanic polymorphism).
*Java supports both method overloading and method overriding
'''
'''
class x:
    def m1(self):
        print("from super class")

class y(x):
    def m1(self):
        print("from derived class")

y1=y()
y1.m1()
'''
class x:
    def m1(self,a,b):
        print("from super class")

class y(x):
    def m1(self,a):
        print("from derived class")

y1=y()
y1.m1()
#here no of arguments in class x != class y. so method overloading happening instead method over riding

