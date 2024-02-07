#Absraction

'''
the concept of hinding the data and methods from one class to another class or out side the class is known as abstraction
-->add __ at the beginning of the property.
'''
class test:
    __x=2000     # here x is hidden,it can be accessed with in the class
    y=3000
    print("x value=",__x)
    print("y value=",y)
    def display(self):
        print("sample __x ",type(test.__x))
        print("sample y ",type(test.y))

s1=test()
s1.display()
print(test.__x)
class sample:
    a=300
    print(a)
    def show(self):
        print("sample __x ",test.__x)
        print("sample y :",test.y)
s2=sample()
s2.show()
