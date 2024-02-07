import threading
class x(threading.Thread):

    def run(self):
        for p in range(50):    #threading 2
            print(p)
#end of class

X=x()
#X.run()
X.start()
for q in range(50,100):   #threading 1
    print(q)

#Multi threading
'''we have to imoprt a in built module (threading)
(threading.Thread)-> it indicates that 'Thread' is the class extending the in bulit class of threading just like inheritance
defining run  method will replace the run method in builtin thread module
whatever the logic or code should be executed should be placed in run method
statements written out of the class is considered as threading 1
statements written with in the run methos is called thrading 2
if we want to execute the threading 1 and threading 2 parallely we need to give X.start()'''
