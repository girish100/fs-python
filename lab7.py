#print **** 4 times with range and without range and using while loop, nested loops can be used
print("/nCase 1: Using range()")
n = int(input("Enter a number: "))
for i in range(n):
    for i in range(n):
        print("*",end="")
    print()
print("\nCase 2:Without using range()")
a = str(n)*n #only for n values 0 to 9
print(a)
for i in a:
    for j in a:
        print("*",end='')
    print()
print("\nCase 3: Using while loop")
b = 0
while b<n:
    c = 0
    while c<n:
        print('*',end='')
        c += 1
    print()
    b += 1
print()
# remove duplicates from string "software engineer"
str1 = 'software engineer'
str2=''
print(str1)
for i in range(len(str1)):
    if str1[i] not in str2:
        str2 += str1[i]
print("After removing duplicate letters in 2 ways: ")
print(str2)
str3 = ''
for j in str1:
    if j not in str3:
        str3 += j
print(str3)
print()
# read <.py> 20 30 40 50 and print sum 
from sys import *
print(argv)
sum = 0
for i in argv[1:]:
    sum = sum + int(i)
print("sum:",sum)
print()
# read product info from the keyboard and if price greater than 25000 add 15% GST and print the new price

print("\nEnter the customer details:\n")
id = ['id']
name = ['name']
product2 = ['product']
price2 = ['price']
dop = ['dop']
for i in range(2):
    cid = eval(input("Enter your customer id: "))
    id.append(cid)
    cname = input("Enter your name: ")
    name.append(cname)
    product = input("Enter your product: ")
    product2.append(product)
    price = float(input("Enter price of the product: "))
    if price > 25000:
        print("Price greater than 25000, 15% GST is applied")
        price= price/100 * 15 + price
        price2.append(price)
    else:
        price2.append(price)
    do_purchase = input("Enter product purchase date: ")
    dop.append(do_purchase)
    print()
print()
print("ID Name Product Price Date of purchase")
for x1,x2,x3,x4,x5 in zip(id,name,product2,price2,dop):
    print("ID:",x1,"||Name:",x2,"||product name",x3,"||price: ₹",x4,"||Date of purchase",x5)
print()
#====================
l1 = eval(input("Enter a list of numbers in list form: "))
def sum_func():
    s =0
    a =0
    while a<len(l1):
        s = s+ l1[a]
        a +=1
    print("sum:",s)
def dup_obj():
    l2 = []
    for i in range(len(l1)):
        if l1[i] not in l2:
            l2.append(l1[i])
    print(l1)
    print(l2)
def odd_nos():
    for j in range(len(l1)):
        if l1[j]%2 == 1:
            print("Odd no. : ",l1[j])
def add_5000_odd():
    b = 0
    while b < len(l1):
        c = 0
        if l1[b]%2 == 1:
            c = l1[b] + 5000
            print("New odd value: ",c)
        b += 1
def extract():
    for k in l1:
        print(k)
print()
sum_func()
print()
dup_obj()
print()
odd_nos()
print()
add_5000_odd()
print()
extract()
print()