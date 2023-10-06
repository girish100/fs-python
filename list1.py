#List data type and list function
print("====LIST DATA TYPE====")
l1 = [100,"abc","16-8-23",100+19j,124.35]
print('the list is :',l1)
print()
print("type of l1 is : ",l1)
print()
for i in l1:
    print(i,type(i))
print()
l2 = list('12')
print(l2)
l3 = l1+l2
print(l3)