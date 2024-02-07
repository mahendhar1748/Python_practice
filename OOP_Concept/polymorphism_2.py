'''
class rbi:
    def minibal(self):
        minbal=0
        print("rbi min bal:",minbal)
class hdfc(rbi):
    def minibal(self):
        minbal=1000
        print("hdfc min bal:",minbal)
class axis(rbi):
    def minibal(self):
        minbal=500
        print("axis min bal:",minbal)
class sbi(rbi):
    def minibal(self):
        minbal=0
        print("sbi min bal:",minbal)

h1=hdfc()
h1.minibal()
'''
#Super Class :- is used to call superclass method through subclass method.

class rbi:
    def minibal(self):
        minbal=0
        print("rbi min bal:",minbal)
class hdfc(rbi):
    def minibal(self):
        super().minibal()
        minbal=1000
        print("hdfc min bal:",minbal)
class axis(rbi):
    def minibal(self):
        minbal=500
        print("axis min bal:",minbal)
class sbi(rbi):
    def minibal(self):
        minbal=0
        print("sbi min bal:",minbal)

h1=hdfc()
h1.minibal()
