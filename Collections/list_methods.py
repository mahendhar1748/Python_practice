#List Methods

x=[10,20,30,40,45]
print(x,type(x),len(x))

#1.Append()
'''Append is used for adding(appending) extra element at the end of the list'''
x.append(50)
print(x,len(x))

#I want to add multiple elements in a list then go with for loop

for p in (55,60,65,70):
    x.append(p)
print(x,len(x))

#2.Extend
'''for extending the list of a another list'''
y=[10.5,20.5,30.5,40.5]
x.extend(y)
print(x,len(x))

#**both append & extend adds the elements at the end of the list**

#3.Insert
'''for inserting an element in desired position (index,value)'''
x.insert(1,15)
x.insert(3,25)
print(x,len(x))

#4.pop(index)
'''for removing an element at index position'''
x.pop(3)
x.pop(5)
print(x,len(x))

#5.Index(element)
'''It returns the index of the e;ement'''
print(x.index(40))

#6.remove
'''It will remove the element'''
x.remove(40)
print(x)

'''
emps=[]
for p in range(1,6):
    x=input("entre the value of String"+str(p)+" ;")
    emps.append(x)
print(emps)
'''

#Remove city field from each and every record
emp=[[101,"miller",6000,"mumbai"],[102,"blake",7000,"hyd"]]

#using pop

for p in emp:
    p.pop(3)
print(emp)

#using remove

for q in emp:
    q.remove(q[2])
print(emp)
















