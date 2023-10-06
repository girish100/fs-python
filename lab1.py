#1.Define a variable. What are the rules of variables. Explain each one with example
print("\n1.Define a variable. What are the rules of variables. Explain each one with example")
print("Variables are containers for storing the data of any data type ")
print("There are five rules for a varibale")
print('''====Rule 1: A variable or identifier must start with alphabets in upper or lower case only,
      a combination of letters and numbers can be used''')
a = 123
A = 'string'
print("A:",A)
print("a:",a)
x1 = 124.56
print("x1:",x1)
set1 = "string 2"
print("set1",set1)
print()
print("====Rule 2: variables are case sensitive and case insensitive ")
print("case sensitive: The address of  variables of are different ")
b = 1900
B = 1200
print("b,id(b) :",b,id(b))
print("B,id(B) :",B,id(B))
print("case insensitive: The address of different variables is same")
q = 2100
Q = 2100
print("q,id(q) :",q,id(q))
print("Q,id(Q) :",Q,id(Q))
print()
print("====Rule 3 : The variable name must not start with special characters except underscore '-'")
_ = 100+100j
print("_:",_)
print()
print("====Rule 4: The size of the variable/identifier is not limited")
Hello_world_python_string_file_in_vs_code = "string name: Hello_world_python_string_file_in_vs_code "
print(Hello_world_python_string_file_in_vs_code)
print()
print("====Rule 5: The variable must not start with reserved keywords defines in python, they are:")
import keyword
print(keyword.kwlist)
print()
#2.What are the fundamental data type? Explain each one with a minimum of 3 examples.
print('2.What are the fundamental data type? Explain each one with a minimum of 3 examples.')
print()
print("int,float,string,complex,boolean : 5 fundamental data types\n")
print()
print("--------int data type------")
x2 = 123
x3 = 321
print('1.',x1,type(x1))
print(x2,type(x2))
sum = x2+x3
print("2.sum is :",sum)
print(type(sum))
mul = x2*x3
print("3.Product is :",mul)
print(type(mul))
print()
print("--------float data type------")
f1 = 123.44
f2 = 132.45
print("1.",f1,f2)
print(type(f1),type(f2))
print("2.sum of float numbers is :",f1+f2)
print(type(f1+f2))
print("3. difference is :",f2-f1)
print()
print("--------string data type------")
name = input("Enter your name: ")
str1 = 'Hello'
str2 = str1+' '+name
print("1.The string concatenation: ",str2)
print("2.String repetition")
str3 = input("Enter another string: ")
print(str3*2)
print("3.slicing the string in +ve and - ve directions")
print("+ve direction:",str2[0:5])
print("-ve direction:",str2[-1:-6:-1])
print("Reverse order: ",str2[::-1])
print("--------Boolean data type------")
b1 = bool(input("enter a value:"))
b2 = bool(input("enter another value:"))
print("1.The values in boolean data type are :",b1,b1)
print(type(b1),type(b2))
print("2.sum of bool is :",b1+b2)
if b1==b2:
    print("3.",b1==b2)
elif b1!= b2:
    print("3.",b1!= b2)
print()
print("--------complex data type------")
c1 = 99 + 8j
c2 = 90 - 12j
print("1.complex numbers are :",c1,c2)
print(type(c1),type(c2))
print("2.The real values are :",c1.real,c2.real)
print("The imaginary values are :",c1.imag,c2.imag)
c3 = eval(input("enter a complex value: "))
mul_c = c1*c2*c3
print("3.The product of complex numbers is: ",mul_c)
print()
#3.Define mutable and immutable objects. Give an example for each
print("Define mutable and immutable objects. Gibe an example for each")
print()
print("""Mutable or state full objects are the types in which data can be modified or changed, 
even after declaring the values in a variable.
list,set,dict,bytearray are some examples of mutable data objects""")
l1 = [12,'mutable',1290.903,'object',361,390]
print()
print("Before modification: ",l1)
l1.insert(-1,"list")
l1.insert(0,'modified')
print("After modification: ",l1)
print()
print("""Immutable or state full objects are the types in which data cannot be modified or changed, 
after declaring the values in a variable.
tuple,frozenset,bytes are some examples of immutable data objects""")
t1 = 10,34,213,58,290
print(t1)
print(type(t1))
print("The above tuple cannot be modified and if tried to modify will result in an error")
print()
#4.Write the differences between list,tuple,set data types with examples
l1 = [1,2,34.4,67,20,39,191,8,0.3,2,4,6.75]
print("1.List is a mutable object and allows indexing and slicing ")
print("the list is:",l1)
print(type(l1))
l2 = [input("Enter a new list: ")]
print(l2)
l1.extend(l2)
l1[2] = 5
print("the updated list is :",l1,type(l1))
print("Indexing an element",l1[0])
print("slicing the list :",l1[::-1])
print()
print("2.Tuple is a immutable object and but allows indexing and slicing ")
t1 = 1,24,0,17,891,9,138,27,34,204.9272
print('The tuple is: ',t1)
print(type(t1))
print(t1[0:5])
print(t1[8])
print()
print("3.set is a mutable object and but does not allow indexing or slicing and duplicate objects ")
s1 = {'1','a','b','word',1001,3850,9082,90.84,1846,8274.9261}
print(type(s1))
s1.add(25)
s1.add('new word')
s1.remove('1')
s1.remove(1001)
print("The updates set is: ",s1)
print(type(s1))
print()
#5.What are the properties of list data type.Explain each one with an example
print("Properties of list:")
print('''1. inseration is preserved
2. list is a mutable object
3. list supports heterogeneous objects
4. it allows duplicate objects
5. it is dynamic and growable
6. indexing and slicing are supported
''')
print()
l1 = [1,2,34.4,67,20,39,191,8,0.3,2,4,6.75]
print("An example list is: ",l1)
#
print("1. inseration is preserved")
l3 = [input("Enter a list : ")]
print(l3)
print(type(l3))
print()
print("2.list is a mutable object")
print(l1)
l1[-1] = 15
l1[-2] = 17
print("after modification: ",l1)
print()
print("3. list supports heterogeneous objects")
l1.append('hello')
l1.append(True)
l1.append(50-89j)
print(l1)
print(type(l1))
print()
print('4. it allows duplicate objects')
l1[0] = 10
l1[1] = 10
l1[2] = 'str'
l1[3] = 'str'
print(l1)
print()
print("5. it is dynamic and growable")
print(l1)
l1.insert(1,92)
l1.pop(-2)
l1.pop(-3)
l1.remove(20)
print("updated list is:",l1)
print()
print("6. indexing and slicing are supported")
print("Indexing : ",l1[-4],l1[0],l1[1])
print("slicing: ")
print(l1[0:5:2])
print(l1[2:7])
print(l1[-1::-1])
print()
print("End of code")