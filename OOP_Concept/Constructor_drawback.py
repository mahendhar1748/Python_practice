#Drawback of Constructor
class sample:
    def __init__(self):
        self.name="Ajay"
        self.age=25
s1=sample()
print(s1.name)
print(s1.age)
s2=sample()
print(s2.name)
print(s2.age)
#here for student2 also the constructor initializes with default values. we need to again modify NSV;s for 2nd object.
s2.name="Amar"
s2.age="26"
print(s2.name)
print(s2.age)
#--------Need of parametarised constructor-------------------------------------
'''
I want different values for each obj during obj creation,then go with parameterised constructor'''
