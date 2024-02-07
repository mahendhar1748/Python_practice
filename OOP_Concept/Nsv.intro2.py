#Non-static variables.
'''
--> the variables which are declared by using name self is called non-static variables
-->if data is changing from one obj to another obj then we go with non-static variables
-->memory is allocated depends upon the object
-->non static variables in a method can be accessed by all the methods using "self"
-->non-static variables with in the method can be accessed by using word self.., and outside the method they can accessed by "s1"
'''
#diff b/w local and non-static variables
'''
->both are defined with in the method only.
->non sttic variables are defined by word self. eg:self.ename=
->local variables are defined with normal eg:ename=
->local variables can't access to other methods.
->but Non-static variables are accessed by all the methods.
'''
#sample program.
class sample:
    x=10
    y=20
    print(x,y)
    def test(self):
        self.x=35
        self.y=45
        print(self)
        print(self.x,self.y)
s1=sample()
s1.test()
print(s1)
