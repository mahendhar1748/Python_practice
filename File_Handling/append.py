#Appending data to the existing file
f3=open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python6.txt",mode='a+')
print(f3.read())
print(f3.tell())
f3.write("This is the data entered for append")
print(f3.seek(0))
print(f3.read())
f3.close()

#Here if we say 'a+', it wont read the data, directly it adds data at the given position.
#Here if we say 'r+', it first reads the data then allows us to append data., how many times we executes the program
#that many times it will append the data
#Both r+ and a+ will creates new file if file doesnt exists.

