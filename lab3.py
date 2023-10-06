#Explain the set properties with examples
print("=====1.Explain the set properties with examples=====\n")
print('''Properties of set:
1.Set does not support insertion
2. Set does not allow duplicate objects
3. set allows heterogeneous objects
4.set is a mutable object
5. set is dynamic and growable
6. Indexing and slicing are not applicable\n
''')
print("1.Set does not support insertion")
s1 =  {'1','a','b','word',1001,3850,9082,90.84,1846,8274.9261}
print("set is : {'1','a','b','word',1001,3850,9082,90.84,1846,8274.9261} \n")
print(s1)
print()
print("2. Set does not allow duplicate objects")
s2 = {1,2,3,4,5,5}
print("s2: {1,2,3,4,5,5} ", s2)
print()
print("3. set allows heterogeneous objects")
print(s1)
print()
print("4.set is a mutable object\n5.set is dynamic and growable")
print("before updating: ",s1)
s1.add(10)
s1.add('new word')
s1.remove('a')
s1.remove('word')
s1.remove(3850)
print("After modification: ",s1)
print()
print("6. Indexing and slicing are not applicable")
print()
#What are the functions involved in set.Write an example for each
print("====2.What are the functions involved in set.Write an example for each.=====")
print("""Functions in set datatype: 
1.add()
2.remove()
3.clear()
4.copy()
""")
print("1.add()")
print(s2)
s2.add(10)
s2.add('new word')
print(s2)
print("2.remove()")
s2.remove('new word')
s2.remove(10)
print(s2)
print("3.clear()")
s2.clear()
print(s2)
print("4.copy()")
s2 = s1.copy()
print("s2")
print()
#What are the list functions.Explain each one with minimum two examples
print("====3.What are the list functions.Explain each one with minimum two examples====")
print("1.append()")
l1 = [1,2,34.4,67,20,39,191,8,0.3,2,4,6.75]
print(l1)
print(" before append(): ",l1)
l1.append(10)
l1.append('a')
l1.append('b')
print("After append(): ",l1,"\n")
print("2.insert()")
l1.insert(0,'insert()')
l1.insert(1,'list')
print(l1,"\n")
print("3.copy()")
l2 = []
print("l2: ",l2)
l2 = l1.copy()
print("l2 after copying l1: ",l2,"\n")
print("4.clear()")
print(l2)
l2.clear()
print(l2)
print("5.extend()")
l2  = [2,3,1,4,5]
print(l2)
print(l1)
l2.extend(l1)
print("After using extend(): ",l2)
print()
print("6.pop()")
obj1 = l2.pop(3)
obj2 = l2.pop(2)
print("pop(): ",obj1,obj2)
print()
print("7.remove()")
l1.remove(2)
l1.remove(20)
l1.remove(39)
l1.remove('a') 
l1.remove('b')
print(l1,"\n")
print('8.sort()')
print(l1)
l1.sort()
print("after sorting",l1,"\n")
print(l2)
l2.sort(reverse= True)
print(l2)
print("9.sorted()")
sort =sorted(l1)
print(sort)
sort = sorted(l1, reverse= True )
print()
#4. what is ment by operator. What is the difference between operator and operand.
#Explain with an example
print("=====4. what is ment by operator. What is the difference between operator and operand====")
print("Explain with an example")
print()
print("operators indicate what action to be taken such as *,+,-,/")
print("operand are the elements on which the operators are used")
print("Ex: 1+2 : ",1+2)
print()
#5.Write a snippet for arithmetic operator ans assignment operator by taking 3 variables
print("=====5.Write a snippet for arithmetic operator ans assignment operator by taking 3 variables=====")
x1 = int("enter an integer x1: ")
x2 = int("enter an integer x2: ")
x3 = int("enter an integer x3: ")
print()
print("arithmetic operator: ")
sum = x1 + x2 + x3
print(sum,"\n") 
print("Assignment operator: ")
x1 += x2
x1 += x3
print(x1)
print()
#6. write 3 snippets for logical 'and' operator & logical 'or' operator
print("====write 3 snippets for logical 'and' operator & logical 'or' operator====")
username = "1"
pass1 = "1"
tnx_id = (1,2,3,4,5,6)
enc_tnx_id = bytearray(tnx_id)
balance = 122000
u1 = input("Enter username: ")
p1 = input("Enter password: ")
pin = int(input("Enter pin: "))
if u1 == username and p1 == pass1 or pin ==1234:
    print("======Verified====== ")
    print("Balance: ",balance)
    v = True
else: 
    print("======Invalid credentials======")
    v = False
details = {'uid':'10001','uname':'banks','uadd':'addess'}
if v == True:
    y = input("Enter yes/no as Y/N for displaying account details: ")
    if y == "y" or y == 'Y':
        for i in details.items():
            print(i)
else:
    print("End of page")
if v == True:
    opt = input("Do you wish to withdraw Y/N: ")
    if opt == 'y' or opt == 'Y':
        wb = int(input("Enter amount to withdraw: "))
        if wb > balance:
             print("Insufficent Balance")
        if wb <= 20000 and pin == 1234:
                print("withdrawl amount : ",wb)
                print("Transction successful")
                balance -= wb
                print("Remaining Balance: ",balance)
        elif pin != 1234:
             print("Invalid Pin")            
        else:
                print("MAX amount is 20000, enter transction id for withdrawl > 20000")
                opt2 = input("Do you wish to enter transction id tuple Y/N : ")
                if opt2 == 'y' or opt2 == 'Y':
                     id1 = eval(input("Enter transction id tuple: "))
                     enc_id1 = bytes(id1)
                     if id1 == tnx_id and enc_id1 == enc_tnx_id:
                          print("Transction successful")
                          balance -= wb
                          print("Remaining Balance: ",balance)
                     else:
                          print("Invalid id")
                else:
                     print("End of an application")
    else:
         print("End of an application")