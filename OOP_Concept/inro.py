class sample:
    x=20
    y=25
    def display(self):
        print("x value :",sample.x)
        z=sample.x+sample.y
        print("z value:",z)
    def emp(self):
        x=30
        print("x value in emp method :",x)
print("static variable",sample.x)
print("static variable",sample.y)

s1=sample()
s1.display()
s1.emp()
        
