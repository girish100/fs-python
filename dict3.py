#using pop function for both list and dict
l1 = eval(input(" list elements: "))
print("Pop() case 1")
p1 = l1.pop(-1)
print("p1:",p1)
print()
print("----case 2----")
l2 = [1,2,4,3,56,7,71,24,6768,90,chr(65),chr(12)]
print("list 2 :",l2)
p2 = l2.pop(-10)
print("pop elements is :",p2,"\n")
print('----case 3----')
for p in l2:
    p=l2.pop()
    print(p)
print()
#pop() case for dict data type
print('pop() case for dict data type')
d1 = {1:1,2:'deccan chronicle','language':'english','design':'timesNR'}
print("dict :",d1)
obj1 = d1.pop(2)
print("the daily name :",obj1)
print("newspaper language:",d1.pop('language'))
print("Text format:",d1.pop('design'))
print()
print("End of application")