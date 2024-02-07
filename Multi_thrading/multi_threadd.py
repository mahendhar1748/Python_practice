#Muliple threadings to be executed parallely

import threading
class x(threading.Thread):

    def run(self):
        for p in range(1,51):    #threading 2
            print(p)

class y(threading.Thread):

    def run(self):
        for r in range(51,200):    #threading 3
            print(r)
#end of class

X=x()
#X.run()
X.start()
Y=y()
Y.start()
for q in range(101,151):   #threading 1(a)
    print(q)
for s in range(151,200):   #threading 1(b)
    print(s)

'''here we need understand the flow of execution
first class x,class y and threading 1(a) executes parallely
threading 1(b) executes independently after them'''

'''If threading 2 execution completed early., threading 1(b) joins in the execution if treading3 or threading 1(a) still
execution'''
