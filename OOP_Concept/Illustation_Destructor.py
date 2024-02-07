# Illustration of Destructor.


class test:
    def __init__(self):
        print("constructor is called")
    def __del__(self):
        print("Destructor is called")
t1=test()   #rc=1
t2=t1       #rc=2
t3=t1       #rc=3

print(t1,t2,t3)

t1=test()   # t1 is the obj again called., so the previous rc decreased by 1. i.e, rc=2
print(t1)

t2=test()   # t2 is the obj again called., so the previous rc decreased by 1. i.e, rc=1
print(t2)

t3=test()   # t3 is the obj again called., so the previous rc decreased by 1. i.e, rc=0
print(t3)

del t1    #obj deleted
del t3    #obj deleted
del t2    #obj deleted
