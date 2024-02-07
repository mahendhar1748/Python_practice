import threading
import time

class x(threading.Thread):

    def run(self):
        time.sleep(10)             #suspending the program for 10 sec
        print("Stopped for 10 sec")
        i=0
        while(i<=10):
            print("hello thread(",i,")")
            i=i+1

    def display(self):
        print("This must should execute 1st")

class y(threading.Thread):

    def run(self):
        time.sleep(15)             #suspending the program for 10 sec
        print("Stopped for 15 sec")

        i=0
        while(i<=10):
            print("hello python,executing (",i,") th time")
            i=i+1
            
t1=x()
t1.start()
t2=y()
t2.start()
t1.display()
time.sleep(5)           #we can stop the main thread also
print("We are running this program to experiment threading (2nd execution)")
            
