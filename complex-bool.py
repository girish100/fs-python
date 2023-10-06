# an example of complex and boolean data types
import time
c3 = complex(input("Enter a complex value: "))
x1 = 100-23j
x2 = 156 + 43J
sum = x1+x2
print("====complex value opearations====")
print()
print("x1 value is :",x1)
print("x2 value is :",x2)
print()
print("type of x1 and x2 is : ",type(x1), type(x2))
print()
print("sum is :", sum)
print()
print(type(sum))
print("real value of sum is :", sum.real)
print()
print("imaginary value of sum is: ",sum.imag)
print()
print("=====boolean operations T/F=====")
resl1 = x1==x2
resl2 = x1!=x2
print(resl1)
print(resl2)
print()
print("type of resl1 is: ", type(resl1))
print()
print("type of resl2 is :", type(resl2))
print()
time.sleep(2)
c1 = eval(input("Enter any complex value c1 : "))
c2 = eval(input("Enter any complex value c2 :"))
print()
print("the value of c1,c2 are",c1,c2)
print("type of c1: ",type(c1))
print("type of c2: ",type(c2))
print()
sum2 = x1+x2+c1+c2+c3
print("sum of complex valuse is : ",sum2)
time.sleep(2)
print("End of code")