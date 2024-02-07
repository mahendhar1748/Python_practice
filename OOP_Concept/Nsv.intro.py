#Non-static variables
'''
-->Non-static variables are always intialized using 'self.'
-->they are purely related to objects
-->memory allowcation depends on object creation.
--->If data is changing from one object to another object.., then we go with non static variables.
---->Non static variables of a class can be accessed by all the methods like static variables
'''
class sample:
    x=100
    y=200
    def display(self):
        self.x=10
        self.y=20
        print("sv:",sample.x)
        print("sv:",sample.y)
        print("nsv:",self.x)
        print("nsv:",self.y)
        print(self)
s1=sample()
print(s1)
s1.display()
'print(sample.x,sample.y,self.x,self.y)'
#while accessing the NSV outside the class, go with reference variable(s1) not self
print(sample.x,sample.y,s1.x,s1.y)
