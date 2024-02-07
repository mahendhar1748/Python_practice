#program to modify static and non-static varibles.
class sample:
    a=4.5
    b=2.6
    def display(self):
        self.x=10
        self.y=20
        print("x= ",self.x)
        print("y= ",self.y)
        print("a= ",sample.a)
        print("b= ",sample.b)
#modifying values
        self.x=self.x+50
        self.y=self.y+50
        sample.a=sample.a+10
        sample.b=sample.b+20
        print("x= ",self.x)
        print("y= ",self.y)
        print("a= ",sample.a)
        print("b= ",sample.b)
s1=sample()
s1.display()
s2=sample()
s2.display()
#Here we need to understand that
'''
->static variables it the old modified values for the next obj calling
->But non-static variables are always intialized as new for new object.
