#Set methods

#add()
'''
--> it will add extra element in set
'''
x={10,20,30,40}
x.add(60)
print(x)

#update()
'''
--> for inserting multiple elemements we use update method
'''
x.update((35,25,65))
print(x)

#copy()
'''
--> for duplicating a set
'''
y=x.copy()  #creates a copy of x
print(x,type(x),id(x))
print(y,type(y),id(y))

z=x  #here z represents x adress
print(z,type(z),id(z))

#pop()
'''removes element randomly'''
x.pop()
print("After pop",x)

#discard()
''' removes selected elemennt'''
x.discard(20)
print("After discard",x)

#clear()
'''it will clear the entire set'''
x.clear()
print(x)





