#---Illustration of inheritence Has_a relation'

class x:
    a=100
    def __init__(self):
        print("a value from calss x:",x.a)
        self.b=200
    def m1(self):
        print("b value from class x :",self.b)

class y:
    c=300
    def m2(self):
        print("c value from class y:",y.c)
        self.x1=x()  #here self.x1 is a local variable used for object creation.
        print(self.x1)
        print(self.x1.b)
        self.x1.m1()    #accessing m1 of class x to class y using NSV
    def m3(self):
        self.z=self.x1.b+x.a+self.c
        print("z value from m3 mehod:",self.z)
y1=y()
y1.m2()
y1.m3()
        
        
