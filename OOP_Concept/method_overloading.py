#method overloading,

'''
->can I have two constructors or two methods in a class with same name...? NO
this is called method overloading (or) constructor overloading

->python does't support method overloading or constructor overloading

eg::
add (a,b,c):
  ----------------
  ----------------
add (a,b):
  ---------------
  ---------------
->****But c,c++,java supports method overloading or constructor overloading.********
'''
class test:
    def __init__(self,p,q):
        self.a=p
        self.b=q
        print(self.a,self.b)
    def __init__(self,x,y):
        self.c=x
        self.d=y
        print(self.c,self.d)
        
t1=test(20,30)
t2=test(200,300)
