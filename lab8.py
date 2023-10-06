#1. Write a code for all arguments with multiple function and execute
def default(a,b,c=10):
    s = a+b+c
    print(s)
    print(b,a,c)
def positional(d,e,f):
    m = d*e*f
    print(e)
    print(f)
    print(d)
    print(m)
if(__name__=="__main__"):
    default(5,6)
    positional(7,8,9)
print()
#2. cla product of 5 arguments
from sys import *
print(argv)
print(type(argv))
a = 1
for i in argv[1:]:
    a *= int(i)
print("Product: ",a)
print()
#3. 1 to 4 table upto 4 multiples 
print("For loop")
for x1 in range(1,5):
    for y1 in range(1,5):
        mul = x1*y1
        print("{}X{}={}".format(y1,x1,mul),end='\t')
    print()
print("While loop")
a =1
while a<5:
    b = 1
    while b<5:
        pro = a*b
        print("{}X{}={}".format(b,a,pro),end='\t')
        b += 1
    a += 1
    print()
