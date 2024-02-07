#removing attributes from sv and nsv

class test:
    """sample program for adding attributes to NSV and SV"""
    x=100
    def sample(self):
        self.y=200

t1=test()
t1.sample()
print(test.x)
print(t1.y)

# adding SV from outside
test.z=300
print(test.z)

#removing attributes of SV
del test.x
del test.z
print(test.z)  #error stmnt bcz not availabe
print(test.x)  #error stmnt bcz not availabe

#adding NSV from outside
t1.a=400
print(t1.a)

#removing NSV
del t1.a
del t1.y
print(t1.a)
print(t1.y)

