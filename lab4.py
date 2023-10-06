# if list objects are even add 10 if list objects are odd subtract 5 using for loop in all 3 forms
l1 = [14,15,12,67,54,23,21,-65,6,-78,93,12,5,19,-3,-5,12,24]
l2 = []
l3 = []
l4 = []
print("\nOriginal List: ",l1,"\n")
#form_1
for x1 in l1:
    if x1%2 == 0:
        x1+= 10
        l2.append(x1)
    elif x1%2 == 1:
        x1 -= 5
        l2.append(x1)
print("FORM_1 : ",l2,"\n")
#form_2
for y1 in range(len(l1)):
    if l1[y1]%2 == 0:
        l1[y1]+= 10
        l3.append(l1[y1])
    elif l1[y1]%2 == 1:
        l1[y1] -= 5
        l3.append(l1[y1])
print("FORM_2 : ",l3,"\n")
#form_3 
for z1 in [14,15,12,67,54,23,21,-65,6,-78,93,12,5,19,-3,-5,12,24]:
    if z1%2 == 0:
        z1+= 10
        l4.append(z1)
    elif z1%2 == 1:
        z1 -= 5
        l4.append(z1)
print("FORM_3 : ",l4,"\n")
if l2 == l3 and l3 ==l4 :
    print("All the three lists are equal\n")
else:
    print("Check the logic in the code for 3 forms\n")