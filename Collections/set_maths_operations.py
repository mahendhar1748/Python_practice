# mathematical operations on sets

'''
--> for performing mathematical operations we have diff options
1.UNION  2.INTERSECTION  3.OR(\)  4.AND(&) 5.DIFFERENCE
'''
a={"ajay","blake","rohith","Miller","james"}
b={"james","pavan","raj","blake","jack"}

print("A = ",a)
print("B = ",b)
#Union  ---> it combines  a and b sets
print(a.union(b))
print(b.union(a))

#Intersection ---> it gives the common elements in both sets
print(a.intersection(b))
print(b.intersection(a))

#Difference  ---> it gives the different element other than other set
print(a.difference(b))
print(b.difference(a))

#OR(\)
print(a | b)  #--> just like union operator

#AND(&)
print(b & a)  #---> just like intersection operator
