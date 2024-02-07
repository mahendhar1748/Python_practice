class sample:
    def __init__(self):
        self.x=100
        self.y=200
        print("initial values ",self.x)
        print("initial values ",self.y)
    def m1(self):
        self.x=self.x+50
        self.y=self.y+100
        print("modified values ",self.x)
        print("modified values ",self.y)
s1=sample()#constuctor executed automatically Nsv created and intialized 
s1.m1()
s2=sample()#constructor executed for the second time Nsv are again intialized
s2.m1()

#for every new object constructor intializes values 
            
        
