#---- Is-A relationship---------------------------------------
'''
-In python we can implement inheritence by using Is-A relation ship
-here without class name or module name we can implement properties of one class to the another class
-inheritence is nothing but deriving a new class from existing class
-BASE CLASS:- It is a class from which new classes are implemented
-DERIVED CLASS:-It extends the base class
'''
#eg:-
'''
class A:
    a=10
    b=20
    def m1(self):
        pass
class B(A):
    c=30
    d=40
    def m2(self):
        pass
b1=B()

-there are two variables in class A and 1 method
-class B is extending class A, class B(sub-class) can access the all the properties of class A
-hence, there are 4 variables in class B and 2 methods.
'''
class A:
    a=10
    b=20
    def m1(self):
        self.x=4.5
        print("from main/base class")
        print(A.a,id(A.a))
        print(A.b)
        print(self.x,id(self.x),type(self.x))
        
class B(A):      #class B extending class A
    c=30
    d=40
    a=50         # overriding happens if we again declares a variable
    def m2(self):
        print("from derived class")
        print(" a value a in class B",B.a)
        print(B.a,B.b,B.c,B.d)

b1=B()
b1.m2()
b1.m1()
    
    












