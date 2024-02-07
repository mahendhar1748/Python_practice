#Garbage collector

'''
-It is a background program/application it executes when the reference count is equal to 0
-It removes the unreferred object automatically when rc=0
'''
# Del
'''del is a key word, which is used to decrease the refernce count of an object
-as we know del it self doesn't removes the object.
'''
# Reference count
'''
no of ref variables ponting towards an object gives the reference count
'''
class test:
    pass
t1=test()  #here t1 is the ref varaible ponting to an obj. so RC=1
del t1     #means it decreases the ref count by 1, so  RC=0

#whenever any obj rc=0, then the obj is removed by garbage collector automatically.
# whenever any obj is going to be removed.., then destructor is called automatically.

class test1:
    pass
c1=test1()  #rc=1
c2=c1       #rc=2

'''here two variables c1 & c2 are pointing the same obj., so ref count =2'''
del t1   #rc=1
del t2   #rc=0
