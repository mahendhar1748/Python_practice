#eg:1 :-reading a file and writing it into another new file  

f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python.txt",mode="r")
n=f.readlines()
q="".join(n)
print("data from old file ")
f.close()
#writing it into a diff new file
f1=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python4.txt",mode="w")
f1.write(q)
f1.close()
f2=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python4.txt",mode="r")
print(f2.read())
f2.close()
print("data from new file: ")
print(" ")
print("files closed")



'''
#eg:2 :-writing into a file
f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python2.txt",mode="w")
''''''variable=hello world
          this is file handling program for writing data
          here variable stores this data
          
f.write(variable)
#f.read()
f.close()
print("file written successfull...")
#now reading a file
f1=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python2.txt")
print(f1.read())
f1.close()
print("file readed and closed")
'''
