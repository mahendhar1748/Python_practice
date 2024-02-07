#Temporarly Suspending the execution of a thread
'''
we can temporarly suspend the execution of a thread by time module
we can sleep the execution in sec '''



import threading
import time                           #importing time module for temporarly suspension
class x(threading.Thread):

    def run(self):
        for p in range(1,11):    #threading 2
            print(p)
            print("Hello for ",p,"times")

class y(threading.Thread):

    def run(self):
        time.sleep(10)            # we are suspending the execution for 10 sec temporarly
        for r in range(11,21):    #threading 3
            print(r)
#end of class

X=x()
#X.run()
X.start()
Y=y()
Y.start()
for q in range(11,21):   #threading 1(a)
    print(q)
for s in range(21,31):   #threading 1(b)
    print(s)

'''
-> in time module we can suspend the execution for some time#here 10 sec temp
->
'''
