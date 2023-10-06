print("\nCase 1:")
a = int(input("Enter a value: "))
b =int(input("Enter a value: "))
c =int(input("Enter a value: "))
d = int(input("Enter a value: "))
e = int(input("Enter a value: "))
max = max(a,b,c,d,e)
min = min(a,b,c,d,e)
print("Maximum value: ",max)
print("Minimum value: ",min)
print()
print("Case 2: Ternary operator by using for_loop,if-else")
f = int(input("Enter an initial value 1: "))
h = f
for i in range(4):
    g = int(input("Enter a value:"))
    if f >= g and g<=h:
        h = g
    elif f <= g:
        f = g
print()
print("MAX: ",f)
print("MIN:",h)
print()
print("Case 3: List - using for loop ,max(),min()")
l1 = []
for i in range(5):
    k = int(input("Enter a value: "))
    l1.append(k)
print("list of elements is: ",l1)
print("List max element: ",max(l1))
print("List min element: ",min(l1))
print()
print("Case 4 using for loop and if statements")
f = [3,11,10,9]
print(f)
print(type(f),len(f))
a = 0
b = 0
for i in f:
    if i>a:
        b = a
        a = i
    if a>i and b<i:
        b = i
print("1st Largest: ",a)
print("2nd Largest: ",b)
print()