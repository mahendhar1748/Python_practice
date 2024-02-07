#---types of Inheritance--------------------------------------------------------

#1) single inheritance
#----------------------

'derived class with single base class'
'''
class x:
    def __init__(self):
        print("from main class")
    def m1(self):
        print("from m1 of class x")

class y(x):
    def __init__(self):
        print("from derived class")
    def m2(self):
        print("from m2 of class y")

y1=y()
y1.m2()
y1.m1()
'''
#2) Multiple inheritance
#------------------------
'A derived class with multiple base classes'
'''
class A:
    x=20
    y=12
    def m1(self):
        print("x=:",A.x)
        print("y=:",A.y)
class B:
    p=20
    q=12
    def m2(self):
        print("p=:",B.p)
        print("q=:",B.q)

class C:
    a=True
    b=False
    def m3(self):
        print("a=:",C.a)
        print("b=:",C.b)

class D(A,B,C):
    def m4(elf):
        print(D.x,D.y,D.p,D.q,D.a,D.b)
d1=D()
d1.m1()
d1.m2()
d1.m3()
print(D.__bases__)
print(B.__bases__)
'''
#3).Multi level Inheritance.
#--------------------------
'Deriving a class from another derived class'

class A:
    x=20
    y=12
    def m1(self):
        print("x=:",A.x)
        print("y=:",A.y)
class B(A):
    p=20
    q=12
    def m2(self):
        print("p=:",B.p)
        print("q=:",B.q)

class C(B):
    a=True
    b=False
    def m3(self):
        print("a=:",C.a)
        print("b=:",C.b)

class D(C):
    def m4(elf):
        print(D.x,D.y,D.p,D.q,D.a,D.b)
d1=D()
d1.m1()
d1.m2()
d1.m3()
print(D.__bases__)
print(B.__bases__)
print(C.__bases__)
print(A.__bases__)



























