#Paramrterised Constructor

'''
->A constructor with parameters is called as paremeterised constructor.Non-static variables are created at the time of object creation.
->How many non-static variables is there that many parameters are specified in the Parameterised constructor
->#**parameters that we are providing in arguments are local variables.it means local var are assigned as non-static variables.
'''
class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(a)
        print(b)
        print(self.a)
        print(self.b)#where a,b are local varibles
    def logic(self,p,q):
        r=p+q
        print(r)
        print(self.a+self.b)
        #print(a+b) ----> as its a local variables didnt have access for another method.

        
s1=test(100,200)#providing data to the varibles at the time of object creation.
s1.logic(500,400)
s2=test(10,20)
s2.logic(100,200)
