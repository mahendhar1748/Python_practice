# we can hide a method also.
'''method we are hiding means.., only it can access with in that class only.'''
# but class we cant hide, class is reusable.

class sample:
    __x=100    # hiding a static variable

    def display(self):
        self.__y=200    #hiding a non-static variable
        print("x value :",sample.__x)
        print("y value :",self.__y)
        self.display2()    # calling a method inside a method
    def display2(self):
        self.z=sample.__x+self.__y
        print(self.z)
        self.__display3()   #calling a method inside a method
    def __display3(self):  #method we are hiding
        self.a=50
        print(self.a)

s1=sample()
s1.display()
print(s1.a)  #it is initialized even though method is hided.bcz display and display2 internally calling display3
