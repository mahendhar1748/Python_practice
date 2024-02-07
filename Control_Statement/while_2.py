#Break and continue
while(True):
    username=input("enter user name: ")
    if(username!="mahi"):
        print("the username is invalid")
        continue
    password=input("enter your password: ")
    if(password=="mahi1748"):
        break
print("login successful")
