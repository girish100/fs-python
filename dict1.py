#dictionary data type
d1 = {'id': 10001, 'name': 'mac n cheese', 'cost': 450, 'location': 'ameerpet', 17:'2'}
print(d1,type(d1))
print()
d2 = dict(id = 20000,name = 'pasta',cost = 250,location = 'ameerpet')
print(d2)
print(type(d2))
print(d2['id'])
print(d2.get('id'))
print("======using dict data type functions======")
print("1.keys()")
print(d1.keys())
for i in d1.keys():
    print(i)
print()
print("2.values()")
print(d1.values())
for i in d1.values():
    print(i)
print()
print("3.items()")
print(d1.items())
print(type(d1.items()))
for i in d1.items():
    print(i,type(i))
print()
print("4.copy()")
d3 = d2.copy()
print(d3)
print()
print("5.clear()")
print(d3)
obj1=d3.clear()
print(d3,obj1)
print()
print("6.get()")
print("names are :",d1.get('name'),d2.get('name'))
print(d1.get('price'),d2.get('price'))
print(d1.get('cost'),d2.get('cost'))
print()
print("7.popitem()")
d3 = d2.popitem()
print(d2)
print('after popitem():',d3)
print(d2)
print()
print("8.pop()")
d1['location'] = 'punjagutta'
print(d1)
d3 = d1.pop('cost')
print(d3)
print(d1)
print()
print("9.update()")
d4 = {}
print(d4,len(d4))
d4.update({'id':30001,'name':'rice n eggs','cost':50,'location':'ameerpet'})
d4.update({'open at':18.00})
d4[10] = 1459
d4[17.9] = 'float num'
print(d4)
print()
print("End  of code")