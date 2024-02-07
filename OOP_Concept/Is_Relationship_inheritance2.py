#-----Eg-2 ---Is-A relationship.---------------
class x:
    def __init__(self):
        print("from main class")
    def m1(self):
        print("from m1 of class x")

class y(x):
    def __init__(self):
        print("from derived class")
    def m2(self):
        print("from m2 of class y")

y1=y()
y1.m2()
y1.m1()

'''
-Here only one constructor executes, derived class methods are overrides the base class this is called polymorpism
'''
