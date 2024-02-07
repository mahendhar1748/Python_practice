# With Statement
'''
with statement will takes care of closing a file that we have opened
with statement follows space indentation '''

data='''
python is implementally easy
python is userfriendly
python is useful in spark and hadoop integration
now a days python got huge demand due to its flexibility
python uses python interpreter that converts .pym code to .py code

'''
'''
with open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python7.txt",mode="w") as f:
    f.write(data)

with open("C:/Users/bairam/OneDrive - Broadridge Financial Solutions, Inc/Documents/test_python7.txt") as f1:
    print(f1.read())
'''
'''
#program to read last n no of a file

file=input("Enter the file path: ")
m=int(input("Enter the no of line to read: "))
n=m+1
with open(file,mode="r") as f:
    print("last ",m,"lines are ")
    for lines in (f.readlines()[-n:]):
        print(lines)
'''
#program to read first n no of a file

file=input("Enter the file path: ")
m=int(input("Enter the no of line to read: "))
n=m+1
with open(file,mode="r") as f:
    print("last ",m,"lines are ")
    for lines in (f.readlines()[:n]):
        print(lines)

