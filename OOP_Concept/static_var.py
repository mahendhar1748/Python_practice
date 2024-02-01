#modifying the static variables

'''
-->if you are modifying static variables that will reflect in all the methods
-->static variables are no way related to objects
-->static variables are always accessed by class name
'''
class sample1:
    x=20
    y=30
    print(x,y)
    '''
    #we can directly print without using class name ,
    #inside class but inside method and outside class.., class name is mandatory
    '''
    def test1(self):
        print("x value: ",sample1.x)
        print("y value: ",sample1.y)
        sample1.x=sample1.x+30
        sample1.y=sample1.y+25
        print(self)
    def test2(self):
        print("x value in test2:",sample1.x)
        print("y value in test2:",sample1.y)
        print(self)
#end of the class
s1=sample1()
#where s1 is called the 'reference variable', it will store the object adress
print(s1)
#print(self)
s1.test1()
s1.test2()
s2=sample1()
print(s2)
s2.test1()
s2.test2()
        
