#typecasting and using eval functions
import time
x1= int(input("Enter a value:"))
x2 =input("Enter a float value:")
e1 = eval(input("Enter any value: "))
f1 = float(x2)
f2 = float(x1)
print(x1,x2,f1,f2)
print(type(x1))
print(type(x2))
print(type(f1))
print(type(f2))
f3 = f1+f2
print()
print("f1+ f2 =", f3)
print()
print("Value of E1 is: ", e1)
print()
print("type of E1 is:", type(e1))
time.sleep(2)
print('end of code')