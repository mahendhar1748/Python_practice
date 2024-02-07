'''
f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python.txt",mode="r")
print(f.read())
f.close()
print("file closed")
#print(f.read())
'''
#opening ,multiple files at a time
'''
f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python.txt")
#even though if we didnt give any mode, it will open default in read mode
f1=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python2.txt")
f2=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python3.txt")
print(f.read())
print(" ")
print(f1.read(),"\n")
print(f2.read())
f.close()
f1.close()
f2.close()
'''
'''
#opening a file in for loop
f3=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python3.txt")
for x in f3:
    print(x)
    #print(" ")
f3.close()
#here x takes 1st line in f3 i.e., in test_python3 file, then 2nd line , and next line until for all lines
'''
#for loop 2

f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python.txt")
#even though if we didnt give any mode, it will open default in read mode
f1=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python2.txt")
f2=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python3.txt")

#keeping all functions in one list

x=[f,f1,f2]

for p in x:
    for q in p:
        print(q)
    print(p.close())
    print("file ended., another file opened")
print("all files opened")
f1.read()


