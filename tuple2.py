l1 = [2,3,4,56,789]
t1 = (14,36,98,472,5674)
print("the list is :",l1)
print("type is :",type(l1))
print()
print("List is mutable and dynamic")
print("displaying only certain elements: ",l1[1:5])
l1.append('A')
print("we can add a new element such as 'A': ",l1)
print()
print("the tuple is :",t1)
print("tuple is immutable hence no new elements cannot be added one the tuple is declared")
# t1[0] = 75 # gives error: (TypeError: 'tuple' object does not support item assignment)
print("Type is: ",type(t1))
print()
print("indexing and slicing is supported: ")
print(t1[0])
print("slicing in -ve direction",t1[-1:-5:-1])
print()
print('''List is a mutable data type, is can be used to change data when ever needed
such as in student or employee info''')
print()
print('''Tuple is a immutable data type, it cannot be changed once declared 
this is useful for fixed info or the ones which do not need to be updated
ex: bank transctions, recording of certain events info ''')