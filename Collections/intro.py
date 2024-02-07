#--------TUPLES-------------------------------------

'''
--> tuples are just like lists, they are represented  by (),
--> tuples are collection data type, which holds group of data
--> tuples are immutable(not going to allow any modification)
--> tuple allows duplicates
--> the order they inserted, the same they retreived
--> tuples allows both, homogenious and hetrogenious elements
--> tuples are also be created by using tuple() function
'''
# But elements of tuples are mutable or immutable

x=(10,20,30,"james",[1,2,3])

print(x[0],type(x[0]))
print(x[3],type(x[3]))
print(x[4],type(x[4]))

#-----> here x[4] is list, we can make modifications to that list

x[4].append(50)
print(x[4],type(x[4]))
print("\n")
#----------------------- creating tuples ---------------------------------------

#1.
a=(1,2,3,4,5,6)
print(a,type(a),len(a),id(a))
print("\n")
#2.
b=(1,2,3,"srting123",4.5,{23,67,89})
print(b[0],type(b[0]))
print(b[3],type(b[3]))
print(b[4],type(b[4]))
print(b[5],type(b[5]))
print("\n")

#3.
z=25,35,45
print(z,type(z),len(z),id(z))
print("\n")

#4.
cities="hyderabad","pune","mumbai","chennai","bengalore"
print(cities,type(cities),len(cities))
print("\n")

#5.
#w=("python")
w=tuple(["python"])
#if there is only one element.., then it is not tuple
print(w,type(w),len(w))
print("\n")

a=["python"]
#if there is only one element.., then it is list only
print(a,type(a),len(a))
print("\n")



#------------------------- creating tuple with tuple function-------------------------------------
X=tuple()
print(X)          #empty tuple got created 
print("\n")

Y=tuple("mumbai")   #each letter is considered as each elememt
print(Y,type(Y),len(Y))
'''
m=tuple("hyd","goa")
print(m,type(m),len(m))

#error ;;TypeError: tuple expected at most 1 argument, got 2
#bcz tuple accepts only one arguments
'''
n=tuple(["hyd","goa"])
print("\n")
print(n,type(n),len(n))
#here we are passing list elements to a tuple, type casting is happenenig

o=tuple((10,20,30))
print(o,type(o),len(o))

'''
--> if we pass a string to the tuple() function, then each character of a string will be taken as element of tuple
--> if we pass a collection to a tuple(), then each element will be considered as the elemnt of tuple
'''
