# 1.write a code to print DOB in formatted string, end attribute, seperator attribute
print("\n1.write a code to print DOB in formatted string, end attribute, seperator attribute")
dd = eval(input("Enter day in date dd: "))
mm = eval(input("Enter month mm: "))
if mm > 13:
    print("invalid month")
else:
    yy = eval(input("Enter year yyyy: "))
    print("Formatted sting form: ")
    print("DOB: {}/{}/{}".format(dd,mm,yy),"\n")
    print("End attribute: ")
    print("DOB",dd,end='/')
    print(mm,end='/')
    print(yy)
    print("\nseperator attribute:")
    print("DOB",dd,mm,yy,sep='/')
print()
print('=========================================================================================================================')
#2.What is the difference between *a and **a
print("2.What is the difference between *a and **a")
def var_arg(*a):
    print(a)
    print(type(a))
    print("*a is used to identify variable length argument and prints output in Tuple data type")
def key_var_arg(**a):
    a.update(d1)
    print(a)
    print(type(a))
    for x1,x2 in a.items():
        print(x1,'---',x2)
    print("*a is used keyword variable length argument and prints output in dict data type as a form of key and value pairs")
if(__name__=="__main__"):
    var_arg(1,2,"h34",129+9j)
    print()
    d1 = {1:2,2:3}
    key_var_arg(num1=2,two=21,sum=23)
print()
print('=========================================================================================================================')
#3.Write a code for each variable length argument and keyboard variable length argument. How outpyt will be returned?
print("3.Write a code for each variable length argument and keyboard variable length argument. How outpyt will be returned?")

def var_len(*b):
    print(*b)
    print(type(b))
    s = 0
    for i in b:
        s = s+i
        print("sum:",s)
def key_len(**b):
    print(b)
    print(type(b))
    s = 0
    for j in b.values():
        s += j
    print("Sum of values of dict data type: ",s)
if(__name__=="__main__"):
    var_len(1,2,3,4)
    key_len(num=23,set=21)
print()
print('=========================================================================================================================')


# 4.write codes for list comprehension, set comprehension, tuple comprehension, dict comprehension
print("4.write codes for list comprehension, set comprehension, tuple comprehension, dict comprehension")
n = 2
c = 5
print("\nList comprehension:")
p=0
q=0
r=0
s = 0
l1 = [x*x  for x in range(n,c+1) ]
print(l1)
for x in l1:
    s += x
print("The sum of list items is : ",s)
print("\nSet comprehension:")
s1 = {x*x for x in range(n,c+1)}
print(s1)
for x in s1:
    p += x
print("The sum of set items is : ",p)
print()
print("\nTuple comprehension:")
t1 = (x*x  for x in range(n,c+1))
print(*t1)
for x in t1:
    q += x
print("The sum of tuple items is : ",q)
print()
print("\nDict comprehension:")
d1 = {x:x*x for x in range(n,c+1)}
print(d1)
for x in d1.values():
    r += x
print("The sum of dict values is : ",r)
print()
print("Lambda function:")
t = 0
la = lambda x:x*x
for x in range(n,c+1):
    print(la(x),end=" ")
    t += la(x)
print("The sum is",t)
#5. traffic lights

def red():
    print("===Stop===")
def green():
    print("===Go===")
def orange():
    print("===Ready to stop / Go===")
print()
while True:
    str1 = input("Enter \Red\nGreen\nOrange\nExit: ").lower()
    if str1 == 'red':
        red()
    elif str1 == 'green':
        green()
    elif str1 == 'orange':
        orange()
    elif str1 == 'exit':
        break
    else:
        print("===Invalid input===")
print()