#--------INHERITENCE--------------------------------
'''
-using the properties of one class to the another class is nothing but inheritance,
-we can aquire all the properties but not hidden properties.
-there are two types of inheritances
i)Has-a relationship
ii)Is-a relationship

---> python uses Is-a relation ship

'''

#--Illustrating Has-a relationship

class A:
    x=20
    def __init__(self):
        self.y=30
        print("x value :",A.x)
        print("y value :",self.y)
    def m1(self):
        print("message from class_A, method m1")

class B:
    a1=A()
    a1.m1()
    print("from A class x value is",A.x)
    z=A.x+a1.y
    print("z value is :",z)
b1=B()
#a1.m1() ----> we can't define outside the class.
#b1=B()
