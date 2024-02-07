#Global variable:it is defined outside the class and outside the method
#Local variable:it is defined inside a function/method.can be accessed within the function/method only
#Static variable:it is defined inside a class and outside a method, can be accessed by class name.
#Local variable: it is defined inside a method and inside a class, can be accessed by object.
r=30
class sample:
    x=30
    y=45
    print(x)
    print(y)
#even though x,y are static variables we can access them without using class name.
#if we are using them inside method (or) outside class then only we can use class name.
    print(r)
    def test(self,p,q):
        #modifying the global variable
        global r #forward declaration
        r=50
        z=p+q+r
        '''where z,p,q are local variables'''
        print("z value ",z)
        w=sample.x+sample.y
        print(w)
s1=sample()
s1.test(20,40)
