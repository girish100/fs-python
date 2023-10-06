from functools import *
s = {4,92,10,3,10,20,10,3,14,5,2}
print(s,type(s))
l3 = reduce(lambda a,b:a+b,s)
print(l3)
#namefull function with reduce()
def func(a,b):
    return a*b
if(__name__=="__main__"):
    
    n = {1,2,4,5,6}
    n = frozenset(n)
    print(n,type(n))
    s1 =reduce(func,n)
    print(s1)