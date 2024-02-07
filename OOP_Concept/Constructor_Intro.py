#Program to access Static Variables and Non-static variables.
class sample:
    a=4.5
    b=5.5
    print(a,b)
    def display(self):
        self.x=10
        self.y=20
s1=sample()
'''
print(s1.x)
print(s1.y)
'''
#here we are not calling 'display' method so the non-static variables are not declared
#where as static variables are declared with the class
s1.display()
print(s1.x)
print(s1.y)

'''------------Need of constructor(__init__) -------------------------------------------------------------

-with out calling a method we can intialize non-static variables by 'constructor'
-By using constructor we can allowcate NSV;s during object creation.
'''
#constructor
'''Def::it is a special kind of method which is used to initialize the NSV's of a class at the time of creation of object.
-->for n no of objects, constructor has to execute for n times.
-->it executes automatically when obj is created.
-->constructor is defined by __init__'''

