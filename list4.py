# test cases to add two lists without '+' operator or extend()
import time
l1 = [1,22,5,7]
l2 = [2,4,7,8]
l3 = l1.copy()
l4 = l2.copy()
print("List 1 :",l1)
print("List 2 :",l2)
print()
print("Test case 1")
print("using for loop and append() : ")
j = 0
for i in l2:
    l1.append(l2[j])
    j += 1
print(l1)
print()
print("test case 2")
print("using while loop")
i = 0
j = -1
while i< len(l2):
    l1.pop(j)
    l1.append(l2[i])
    i += 1
    j -= 1
print(l1)
print()
print("test case 3")
print("using if-else")
k = 0
if len(l3) < len(l3+l4):
    l3.append(l4[0:len(l4)])
    k += 1
else:
    print(l3)
print(l3)