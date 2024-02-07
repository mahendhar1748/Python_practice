#Tell amd seek
#tell:- it tells the exact position of a cursor
#seak;- movig the cursor to the desired position


f=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python5.txt")
print(f.tell())
print(f.read())
print(f.tell())
f.seek(10)
print(f.tell())
print(f.read())
f.close()
