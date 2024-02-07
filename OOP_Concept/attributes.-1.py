#adding attributes to sv and nsv

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

#adding NSV from outside
t1.a=400
print(t1.a)

#creating object 2
t2.sample()
print(t2.y)
print(t2.a)  #here this statement is invalib bcz...
#we added NSV to the t1 object. so t2 object can't access that variable

