#Sets
'''
--> set are represented using {} curly braces
--> set allows homogeneous{12,23,34,56,46} and hetrogeneous{12,34,True,False} elements
--> In sets the order way you inserted..,they are retreived in the same order
--> set doesnt support indexing, print(p[0])
--> set is defined by using set() function
--> Duplicates are not allowed in sets
--> we can do type_casting in sets
--> we cant use while loop for sets.., bcz while loop requires indexing
--> set is mutable but the elements in a set should be immutable. set inside set not allowed
'''
x={23,34,455,567,789,23}
print(x)

y={34,45,456,True,False}
print(y,id(y),type(y),len(y))

z={34,45,56,67,67,89,(23,45)}
print(z,id(z),type(z),len(z))

a=set()
print(a,id(a),type(a),len(a))

b=set("hello")
print(b,id(b),type(b),len(b))

#here set dont displays the duplicates.., so length =4 only

'''
c=set("hai","hello")
print(c,id(c),type(c),len(c))
'''
#here we face an error (TypeError: set expected at most 1 argument, got 2), set function allows only iterable types.
#i.e., strings,lists,tuples

d=set([12,34,345,456,78])
print(d,id(d),type(d),len(d))

e=set((23,45,56,67,78,89,0))
print(e,id(e),type(e),len(e))

#if you pass any collection to the set., then the length of that collection is equal to the length of the set ignoring dups

f={(12,23,23,34)}
print(f,id(f),type(f),len(f))

#for loop in a set
for p in x:
    print(p,type(p))

