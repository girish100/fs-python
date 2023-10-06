#common differences in list and dict data types
import time
l1 = [12,34,'a',ord('Y'),57.09,'py-code',ord('Z')]
d1 = {1:1,2:'name','eng':'eng','design':'timesNR'}
print("\nList:",l1,"type:",type(l1))
print("Dict:",d1,"type:",type(d1),"\n")
print("=====accessing and modifying the lists and dicts")
print("Adding and modifing elements:\n")
l1.append(14)
print("list append() ",l1)
l1.insert(0,12)
print("l1.insert(0,12):",l1)
l2 = [12,121,34,'a']
l1.extend(l2)
print("extend(): ",l1)
#dict update()
d1.update({'new-id':4900})
d1[2] = 10
print("dict update:",d1,"\n")
#====================removing elements/objects======
print("deleting or removing elements")
obj1 = l1.pop(-1)
l1.remove(89)
l1.remove(ord('Z'))
print("l1.remove(89),l1.remove(ord('Z')): ",l1)
print("l1.pop(-2):",obj1)
#d1
obj3 = d1.popitem()
print("d1.popitem()",obj3)
obj4 = d1.pop('eng')
print("d1.pop('eng):",obj4,"\n")
#======accessing the elements====
print('Accessing the elements')
#list l1
print("list access with indexing and slicing:")
print("Using slice operator",l1[0:4])
print("Using indexing:",l1[-5])
print()
#dict d1
print("dict element access")
print("By specifying key d1.[key_name/num]:",d1['design'])
print("By specifying keys in get():",d1.get(2)) #get() takes only one key name
print("displaying only keys :",d1.keys())
print('displaying only values:',d1.values(),"\n")
# copy() and clear()
print("======Using copy() and clear()=====")
print("list and dict have same syntax to copy or clear")
print("variable_2=variable_1.copy() & variable.clear()\n")
d2 = {}
print('dict d2:',d2)
d2 = d1.copy()
print("after copying d1 :",d2)
d2.clear()
print("after using clear():",d2,"\n")
l3 = []
print('list l3:',l3)
l3 = l2.copy()
print("after copying l2 :",l3)
l3.clear()
print("after using clear() :",l3)
#=======sort() and sorted()
print("List supports both sort() & sorted(), dict can be sorted only by using sorted()")
#l1.sort() #error (not supported between instances of 'str' and 'int')
#print("sorted list :",l1)
#l1.sort(reverse=True) #error (not supported between instances of 'str' and 'int')
#print("Reverse of list:",l1)
#sor =sorted(d1) #error (not supported between instances of 'str' and 'int')
#print("sorted dict:",sor)
#rev_sor = sorted(d1,reverse=True)
#print("Reversed dict:",rev_sor)
#-------------
# dictionary data type with sorted()
d11 = {1:2,17:4,12:23}
print(d11, type(d11))
sor = sorted(d11)
print("s1",sor)
d11 = {1:2,17:4,12:23}.values()
sor2 = sorted(d11)
print("s2",sor2)
d11= {1:2,17:4,12:23}.items()
sor3 = sorted(d11)
print("s3",sor3)
time.sleep(2)
print("\n End of application")