# class with four methods
class four_methods:
    def __init__(hello) : #constructor
        print("this is a constructor method")
        hello.pid = 50
    def m2(wor): #instance
        print("This is a instance method")
    @classmethod #classmethod
    def m3(cls):
        print("This is a class method")
        
    @staticmethod #staticmethod
    def m4():
        print("This is a static method")
        
c1 = four_methods() #constructor

c1.m2() #instance calling

c1.m3() #classmethod with object reference varibale.method name()

c1.m4()#staticmethod with object reference varibale.method name()

four_methods.m3()#classmethod
four_methods.m4()#staticmethod 