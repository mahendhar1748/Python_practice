#----------------customer application -------------------------------------
class customer:
    bank="SBI"
    def __init__(self,name,accno,addrss,bal):
        self.cname=name
        self.caccno=accno
        self.caddrss=addrss
        self.cbal=bal
        #how many constructor parameters are defined,those many NSV's should be drfined.
    #operations
    def deposit(self,depositamnt):
        self.cbal=self.cbal+depositamnt
        print('after depositing ',depositamnt,' total Acc Bal is ',self.cbal)
    def withdraw(self,withdrawamnt):
        self.cbal=self.cbal-withdrawamnt
        print('after withdrawl of ',withdrawamnt,' total Acc Bal is ',self.cbal)
    def balenq(self):
        print('Your total Bal is ',self.cbal)
    def display(self):
        print("customer Bank   :",customer.bank) #Sv always defined with class name
        print("customer name   :",self.cname)
        print("customer accno  :",self.caccno)
        print("customer addrss :",self.caddrss)
        print("customer Bal    :",self.cbal)

c1=customer("Mahendhar",12345,"Hyderabad",24000)
c1.display()
c1.balenq()
c1.deposit(5000)
c1.withdraw(2500)
c1.balenq()

#creating list of customers

customers=[]        #taking an empty list
customers.append(customer("scott",13245,"bengalore",215416))
customers.append(customer("miller",136245,"chennai",212416))
customers.append(customer("virat",13545,"bengalore",215446))

for obj in customers:
    print(obj.display())
    print(obj.withdraw(12416),obj.balenq())







