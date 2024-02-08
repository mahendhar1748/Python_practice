#Functions on sets
x={10,20,30,40,50,60,70}

print(x,type(x),len(x))
print(min(x)) #prints min element
print(max(x))
'''
i we give a tupe like..x={10,20,30,40,50,60,70,(23,45)}.., then some functions may not work
#TypeError: '<' not supported between instances of 'tuple' and 'int'
'''
print(sum(x))
print(sorted(x))
print(sorted(x,reverse=True))

#printing summation without sum function

summation_1=0
for p in x:
    summation_1+=p
print("summation",summation_1)

#printing summation  of first 3 elements
summation=0
count=1
for p in x:
    summation+=p
    count+=1
    if (count == 3):
        break
print("summation",summation)

#searching for a element in set
print(30 in x)
print(80 in x)
#------------------------------------ 0 ------------------------------------------------------------
y={10,20,30,40,50,60,70}

print(x is y) #adresses are equal
print(x == y) #if the cotent is equal

#------------------------ 0 -----------------------------------------------
#packing of set

z={10,20,30,40,50,60,70}
s1,s2,s3,s4,s5,s6,s7=z
print(s3)
