#hiding static and non-static variables.


class sample:
    __x=100
    print("x value : ",__x)
    def test(self):
        self.__y=200
        print("y value :",self.__y)
        print("x value :",sample.__x)
s1=sample()
s1.test()
print(sample.__x)  #can't access to outside of class bcz those are hidden
print(self.__y)    #can't access
