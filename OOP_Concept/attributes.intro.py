#Attributes in python.

'''
-for each and every class in a python,some attributes are going to be add by the python interpreter.
-attribute are added by the python interpreter are called built in attributes,
__bases__
__doc__
__name__
__module__
__dict__

'''
class test:
    """sample class for built in attributes"""
    x=20
    y=30
    def m1(self):
        print(test.x)
        print(test.y)
c1=test()
c1.m1()
print(test.__bases__)
print(test.__doc__)
print(test.__name__)
print(test.__module__)
