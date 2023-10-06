#dict comprehension
print("\nDict comprehension")
d1 = {num:num*num for num in range(1,15)}
print(d1)
for x1,x2 in d1.items():
    print(x1,'--',x2)
print()
#set comprehension
print("\nSet comprehension")
s1 = {x1*x1 for x1 in range(1,11)}
print(s1)
s2 = {x2*x2 for x2 in range(1,11)if x2%2 == 0 }
print(s2)
print()
#list comprehension
print("\nlist comprehension")
l1 = [x1*y1 for x1 in range(1,10) for y1 in range(1,11)]
print(l1)
print()
#tuple comprehension
print("\ntuple comprehension")
t1 = (z1**z1 for z1 in range(1,11))
t2 = (z1**z1//10 for z1 in range(1,11))
t3 = (z1**z1%10 for z1 in range(1,11))
print(t1)
print(*t1)
print(*t2)
print(*t3)
print()