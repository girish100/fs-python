#global variable
gv = 120 #eval(input("Enter a number: "))  # gv is a global variable as it is declared outside a function
print("Global variable",gv)
def test1():
    gv = 10 #local variable
    s = gv * 10
    print("lc",gv*8)
    return s

#local variable
def test2():
    lv = 15 # lv is a local variable as it is declared inside a function
    lv = gv + lv #can't dp gv = gv + lv

    print("Updated local variable: ",lv)
    return lv
test1()
print("local variable modified",test1())
test2()
print("Local variable: ",test2())

#nameless function
from functools import reduce
nl = lambda x:x**x 
print("Exponent: ",nl(4))
nl1 = lambda str1:input("Enter a string: ")
print(nl1(str1=''))
l = 's t r i n g'
nlr = reduce(lambda n,y:n+y,l)
print(nlr)