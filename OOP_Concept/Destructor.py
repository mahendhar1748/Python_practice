# Destructor

'''
whenever an obj is going to be removed.., then the Destructor executes automatically

   __del__(self)
     ---------------------------
     ---------------------------
'''
class test:
    def __init__(self):
        print("constructor is called")
    def __del__(self):
        print("Destructor is called")
t1=test()   #rc=1
t2=test()   #rc=1
t3=t1       #rc=2

print(t1,t2,t3)

del t1    #rc=1
del t3    #rc=0
del t2    #rc=0
