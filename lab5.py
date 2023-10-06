#1. write a code for customers who have won amount when entering the following numbers:
'''a) 4678------> "You have won ₹289/-"
b)5298 --- 598
c)8234 --- 666
d)4923---789
apart from these values, the customeers must get "Better luck next time"
'''
#--------
print("\n 1. write a code for customers who have won amount")
tnum = eval(input("\nEnter your ticket number : "))
print()
if tnum == 4678 or tnum == '4687':
    print("You have won ₹289/-")
elif tnum == 5298 or tnum == '5298':
    print("You have won ₹598/-")
elif tnum == 8234 or tnum == '8234':
    print("You have won ₹666/-")
elif tnum == 4923 or tnum == '4923':
    print("You have won ₹789/-")
else:
    print("Better luck next time")
print()
#2. write a code to print 'A to Z' and 'a to z' by using range data type. Hint: ASCII values
print("\n2. write a code to print 'A to Z' and 'a to z' by using range data type.")
print("\nUpper case alphabets: ",end="")
for i in range(65,91):
    print(chr(i),end = ' ')
print("\nLower case alphabets: ",end="")
for i in range(97,123):
    print(chr(i),end =' ')
print()
print("Type - 2: ",end=" ")
for i in range(65,123):
    if i not in range(91,97):
        print(chr(i),end=" ")
print()
#3. Enter the customer details of 5 records by using for loop.
print("\n3. Enter the customer details of 5 records by using for loop.")
d1 = {}
id = ['id']
name = ['name']
product2 = ['product']
price2 = ['price']
dop = ['dop']
for i in range(5):
    cid = eval(input("Enter your customer id: "))
    id.append(cid)
    cname = input("Enter your name: ")
    name.append(cname)
    product = input("Enter your product: ")
    product2.append(product)
    price = float(input("Enter price of the product: "))
    price2.append(price)
    do_purchase = input("Enter product purchase date: ")
    dop.append(do_purchase)
    d1.update({"Customer ID":cid,'custome name':cname,'Product name':product,'price':price,"Date of purchase":do_purchase})
print("\n====Last customer details====")
for x1,x2 in d1.items():
    if x1 == 'price':
        print("price:",'-',"₹",x2)
    else:
        print(x1,"-",x2)
print()
print("ID Name Product Price Date of purchase")
for x1,x2,x3,x4,x5 in zip(id,name,product2,price2,dop):
    print(x1,x2,x3,x4,x5)
print()
     #print("ID:{}\tName:{}\tProduct:{}\tPrice:{}\tDate of purchase:{}".format(id,name,product2,price2,dop))
print()
#4. Write a code for Metro Station in hyderabd with fare b/w two stations as starting point and ending point
"""print('''1. Ameerpet\t2. SR Nagar\t3.Punjagutta\t4.Begumpet
5.MGBS\t 6.Miyapur\t7.Parade Ground \t 8.Nagole
9.Raidurg\t10.LB Nagar\t11. KPHB\t12.Uppal''')
s1 = ['Mipapur',1]
s2 = ['KPHB',2]
s3 = ['Ameerpet',3]
s4 = ['Begumpet',4]
s5 = ['Punjagutta',5]
s6 = ['SR Nagar',6]
s7 = ['Parade Ground',7]
s8 = ['Nagole',8]
s9 = ['Raidurg',9]
s10 = ["MGBS",10]
s11 = ['Uppal',11]
s12 = ['Nagole',12]
p1 = input("Enter starting point: ").lower()
p2 = input("Enter destination: ").lower()
print()
if p1 == 'ameerpet' or p1 == '1' or p1=='srnagar' or p1 == 'sr nagar':
    if p2 == 'sr nagar' or p2 == 'srnagar' or p2 == '2' or p2 == 'ameerpet':
        print("Ticket Fare b/w %s and %s is ₹10"%(s1,s2))
if p1 == 'ameerpet' or p1 == '1':
    if p2 == 'punjagutta' or p2 == '3':
        print("Ticket Fare b/w %s and %s is ₹10"%(s1,s3))
    elif p2 == 'begumpet' or p2 == '4':
        print("Ticket Fare b/w %s and %s is ₹10"%(s1,p2))
    elif p2 == 'mgbs' or p2 == '5':
        print("Ticket Fare b/w %s and %s is ₹35"%(s1,p2))
    elif p2 == 'miyapur' or p2 == '6':
        print("Ticket Fare b/w %s and %s is ₹40"%(s1,p2))
    elif p2 == 'Parade Ground' or p2 == '7' or p2 =='paradeground':
        print("Ticket Fare b/w %s and %s is ₹35"%(s1,p2))
    elif p2 == 'nagole' or p2 == '8':
        print("Ticket Fare b/w %s and %s is ₹40"%(s1,p2))
    elif p2 == 'raidurg' or p2 == '9':
        print("Ticket Fare b/w %s and %s is ₹45"%(s1,p2))
    elif p2 == 'kphb' or p2 == '10':
        print("Ticket Fare b/w %s and %s is ₹35"%(s1,s1))
    elif p2 == 'uppal' or p2 == '12':
        print("Ticket Fare b/w %s and %s is ₹40"%(s1,s12))"""

print("Stations list ")
print('''1. Ameerpet\t2. SR Nagar\t3.Punjagutta\t4.Begumpet
5.Nagole\t 6.Miyapur\t7.Parade Ground \t 8.MGBS
9.Raidurg\t10.LB Nagar\t11. KPHB\t12.Uppal''')

l1 = ['ameerpet','sr nagar','punjagutta','begumpet','nagole','miyapur','parade ground','mgbs','raidurg','lb nagar','kphb','uppal']
s1 = input("Enter starting point: ").lower()
s2 = input("Enter destination: ").lower()
if (s1 == s2):
    print("Starting point and Destination are same, please choose different sations")	
elif s1 not in l1 or s2 not in l1:
	print("Station not in data")
else :
	for i in range(len(l1)):
		if s1 == l1[i]:
			m1 = i
		elif s2 == l1[i]:
			m2 = i
	fare = (m1-m2)*10
	if fare < 0:
		fare = -1*fare
	if fare > 60:
		fare = 60
	print("The fare between %s and %s is ₹%d"%(s1,s2,fare))      