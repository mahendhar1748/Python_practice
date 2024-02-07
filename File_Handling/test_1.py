
#opening a file for reading
'''
f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python4.txt",mode='r')
print(f.read())
f.close()
'''
#Writing into a file and then reading
'''
f1=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python4.txt",mode='w')
data='''
#Hi This is the test file to read and write
#please provide your details
'''
f1.write(data)
f1.close()
#
f2=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python4.txt",mode='r')
print(f2.read())
f1.close()
'''
#Appending data to the existing file
f3=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python5.txt",mode='r+')
print(f3.read())
print(f3.tell(),"/n")
f3.write("This is the data entered for append")
print(f3.seek(0))
print(f3.read())
f3.close()

#Here if we say 'a+', it wont read the data, directly it adds data at the given position.
#Here if we say 'r+', it first reads the data then allows us to append data., how many times we executes the program
#that many times it will append the data

