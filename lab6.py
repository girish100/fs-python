print("\n1.=======Finding 2nd largest number from a list/tuple/set/dict========\n")
f = eval(input("Enter a list/tuple/set/dict: "))
a = 0
b = 0
for x1 in f:  # for negative numbers
    if x1 <= a:
        a = x1
        b = x1
for i in f:
    if i>a:
        b = a
        a = i
    if a>i and b<i:
        b = i
print("1st Largest: ",a)
print("2nd Largest: ",b)
print()
print('\n2. =======Finding a string or numbers is palindrome or not ========= ')
# for finding palindrome in a string
str1 = input("\nEnter a string: ")
str2 = ''
for x1 in str1:
    str2 = x1+str2
print("\nThe reverse of the string is %s "%str2)
if str1 == str2:
    print("The given string %s is a palindrome "%(str1),'\n')
else:
    print("The given string '%s' is not a palindrome "%(str1),'\n')
# finding a palindrome in a number
num = eval(input("Enter a number: "))
n = num
reverse = 0
while n > 0:
    remainder = n%10
    reverse =reverse*10 + remainder
    n //= 10
if (num == reverse):
    print("{} is a palindrome of {}".format(num,reverse))
else:
    print("{} is not a palindrome of {}".format(num,reverse))
#Armstrong number
print("\n======== 3.Finding Armstrong Number or Not=========\n")
num = eval(input("Enter a number: "))
n = num
sum  = 0
while(n>0):
    unit = n%10
    cube = unit**3
    sum = sum + cube
    n //=10
print("sum of the digits cube is :",sum)
if num == sum:
    print("{} is a armstrong number".format(num))
else:
    print("{} is not a armstrong number".format(num))

range1 = int(input("Enter range to find the arms strong numbers upto that number:"))
a = 0
while a <range1:
    num = a
    n = num
    sum  = 0
    while(n>0):
        unit = n%10
        cube = unit**3
        sum = sum + cube
        n //=10
    if num == sum:
        print("{} is a armstrong number".format(num))
    a+=1
# 4. Fibonacci series
print('\n=======4.Fibonacci series======\n')
a = 0
b = 1
n = int(input("Enter range to print fibonacci series : "))
r = 0
print("The fibonacci series upto range {}".format(n))
print(a,b,end=' ')
while r<n:
    c = a+b
    a = b
    b = c
    print(c,end=' ')
    r += 1
print()
#5. Reverse of a string
print("\n========5.Reverse of a string==========\n")
str3 = input("Enter a string: ")
str4 = ''
for x1 in str3:
    str4 = x1+str4
print("\nThe reverse of the string is %s "%str3)
print()