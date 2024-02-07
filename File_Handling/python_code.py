f=open("test.py",mode="w")
f.write("x=[10,20,30,40,50]\n")
f.write("print(x,type(x),id(x))\n")
f.write("print(len(x),sum(x))\n")
f.write("x.append(60)\n")
f.write("print(x,type(x),id(x))\n")
#print(f.read())
f.close()
print("file closed successfully")

#method-2
#take a variable.., write the python code and assign it to that variable

#method-3
#we can also read the python file.
