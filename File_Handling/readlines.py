f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python5.txt",mode="r")
x=f.readlines()
print(x,type(x),id(x))
#if we say readlines., internally it creates a list for every line
#printing only names and salaries

for p in x:
    print(p.split(",")[1],p.split(",")[2])
    #print(p.split(",")[1:3])
f.close()
m="".join(x)
print(m)
