#Define slice operator. write the syntax for slice operator
print("\n1.Define slice operator. write the syntax for slice operator")
print(""" def:slice operator is used to display a string in parts as per application requirements
slice operator can be displayed either in forward(+ve) or backward(-ve) direction
""")
print('''slice operator syntax
forward direction: var = 'string_'
                   var[begin:end(end-1):step]
                   ex: var[0:2:1]
backward direction: var = 'string_'
                    var[begin:end(end+1):step] 
                    step value must be -ve
                    ex: var[1:-12:-1]''')
#how many data types are involved in python. Explain each one with an example
#fundamental (5) data types covered in lab1.py
print("\n2.How many data types are involved in python. Explain each one with an example")
print('''Apart from fundamental data types(int,float,str,boolean,complex) the other data types are:
1.list data type
2.tuple data type
3.set data type
4.dict data type
5.frozenset data type
6.none data type
7.range data type
8.bytes data type
9.bytearray data type
''')
print('1.list data type')
l1 = [1,2,34.4,67,20,39,191,8,0.3,2,4,6.75]
print("the list is defined using [] or using list(), example list is:",l1)
print(type(l1),"\n")
print('2.tuple data type')
t1 = 1,24,0,17,891,9,138,27,34,204.9272,'hello',None
print("tuple is declared in () or directly typed :",t1)
print(type(t1))
print()
print('3.set data type')
s1 = {'1','a','b','word',1001,3850,9082,90.84,1846,8274.9261}
print("set is declared in {} or using set() : ",s1)
print(type(s1),"\n")
print('4.dict data type')
d1 = {'id':30001,'name':'rice n eggs','cost':50,'location':'ameerpet'}
print("dict has key:value pair in each object, it is declared either using dict() or {key:value}",d1)
print(type(d1),"\n")
print('6.frozenset data type')
fs = frozenset(s1)
print("frozenset is declared using var = frozenset(<set_variable>), ex:fs = frozenset(str1)")
print(fs)
print(type(fs),"\n")
print('7.none data type')
print("none data type stores None value")
p = 25000
print(p,type(p))
p = None
print(p,type(p),"\n")
print('8.bytes data type')
print("bytes data type has a range of (0,255),\n syntax: var = bytes(var2)")
b = 0,193,82,145,231,83,169,170
by = bytes(b)
print("encrypted form of tuple is :",by)
print("normal form of tuple is :",*by)
print(type(by),"\n")
print("9.byte arryay data type")
print("it is similar to bytes data type except this data type is a mutable data type ")
ba = bytearray(b)
print(ba)
print(*ba)
print(type(ba),"\n")
#Define type casting and how we implement type casting with 5 examples
print("3.Define type casting and how we implement type casting with 5 examples")
print("""Type casting is the process used to convert one data type into another data type,
as per the application requirement

EX:""")
x1 = 10012
print(x1)
print(type(x1))
x1 = float(x1)
print(x1)
print(type(x1))
x1 = str(x1)
print(x1)
print(type(x1))
x1 = list(x1)
print(x1)
print(type(x1))
x1 = set(x1)
print(x1)
print(type(x1))
x1 = tuple(x1)
print(x1)
print(type(x1))
#Apply the following slice operators for the following string
print("\n4.Apply the following slice operators for the following string")
str1 = 'Front End Developer'
print("The string is : ",str1)
print("case 1 str1[2:9] --- prints from index position 2 to 9 in +ve direction:",str1[2:9],"\n")
print("case 2 str1[-7:-23] --- no output as step value is missing for -ve direction:",str1[-7:-23],"\n")
print("case 3 str1[-16:-7] --- prints from index position -16 to -7 in +ve direction:",str1[-16:-7],"\n")
print("case 4 str1[::] --- prints entire string: ",str1[::],"\n")
print("case 5 str1[::-1] --- prints string in reverse oder:",str1[::-1],"\n")
print("case 1 str1[6:8:0] --- Generates an error:","\n")
#Define tuple datatype. Explain the properties of tuple datatype
print("5.Define tuple datatype. Explain the properties of tuple datatype")
print("""Tuple datatype is used when a group of objects or one object as a single entity and do not want to 
change data once declared, then tuple data type is used\n""")
#
print("""Properties of tuple datatype
1.Inseration is preserved (input=output)
2.Tuple allows heterogeneous objects
3.Tuple is immutable
4.it is not dynamic or growable
5.indexing and slicing are applicable
6.duplicate objects are allowed\n""")
print('1.Inseration is preserved (input=output)\n')
t1 = input("enter tuple elements: ")
print("the tuple is:",t1,"\n")
print('2.Tuple allows heterogeneous objects\n')
t1 = 1,24,0,17,891,9,90+112j,138,27,34,204.9272,'hello',None
print(t1)
print()
print('3.Tuple is immutable\n4.it is not dynamic or growable\n')
print("Tuple does not allow modification, if tried results in type error\n")
print("5.indexing and slicing are applicable\n")
print("Indexing: ",t1[0],t1[2],"\n")
print("slicing: ")
print(t1[0:])
print(t1[-1:-6:-1])
print(t1[::-1])
print('6.duplicate objects are allowed\n')
t2 = 1,12,3,3,21,12,1,'word','word',10+11j,10+11j
print(t2)
print()
#What is ment by ordered datatype and unordered datatype. Explain each one with two examples
print('6.What is ment by ordered datatype and unordered datatype. Explain each one with two examples\n')
print("""The datatypes in which the variable retain the order in which elements or objects are placed
are called ordered datatypes. Ex: strings,lists,tuple""")
print()
str2 = input("enter some words:")
l4 = [input("Enter a list: ")]
print(str2)
print(l4)
print()
print("""The datatypes in which the variable do not retain the order in which elements or objects are placed
are called unordered datatypes. Ex: set,frozenset""")
print()
s1 =  {'1','a','b','word',1001,3850,9082,90.84,1846,8274.9261}
print("set is : {'1','a','b','word',1001,3850,9082,90.84,1846,8274.9261} \n")
print(s1)
fs = frozenset(s1)
print("frozenset is : {'1','a','b','word',1001,3850,9082,90.84,1846,8274.9261}")
print(fs)
print()
import time
time.sleep(2)
print("End of code")
