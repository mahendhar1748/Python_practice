#writing into a file with 'W+' mode
#in w+ mode., first it writes the data into a file then it reads

f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python4.txt",mode='w+')
emp=input("Enter the emplyee Details: ")
f.write(emp)
print(f.read())
#After writing the cursor is at last poistion., it will reads empty spaces if we wont bring the cursor to 0th poistion
f.seek(0)
print(f.read())
f.close()
