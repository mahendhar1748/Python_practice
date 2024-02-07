#while loop
'''while loop executes set of statments for related number of times'''
'''statments in the while loop executes no of times until the condtion becomes true'''
'''
#to print 0 to 10
x=0
while(x<=10):
    print(x)
    x=x+1
'''
'''
#sum of first n natural numbers

n=int(input("entre the value:"))
sum=0
x=1
while(x<=n):
    sum=sum+x
    print(sum)
    x=x+1
'''
'''
#break statement

if break statemnet is used in a loop then control comes out of that loop & statement after break are not executed'''
'''
x=1
while(True):
    print('we are in infinite loop')
    if(x==5):
        print('we are comes out of the loop')
        break
    x=x+1
print('end')
'''
#continue
#it skips the current iteration & continius with next statemnt
x=0
while(x<10):
    x=x+1
    if(x==5):
        continue
    print(x,"hello")
print("end")









