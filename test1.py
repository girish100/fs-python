#35 cases using if statement
x1 = eval(input("Enter a number: "))
print('test case 1 ')
if x1<0:
    print("The number is neagtive: ",x1)
if x1>0:
    print("the number is positive: ",x1)
if (x1==0):
    print("the number is zero: ",x1)
print()
print('test case 2 ')
u1 = input("enter username: ")
p1 = input("enter password: ")
pin = int(input("Enter pin: "))
balance = 200000
if u1 == '1' and (p1 == '1' or pin ==1234):
    print("Verified ")
    print("Balance: ",balance)
    v = True
print()
print('test case 3 ')
if u1 != '1' or (p1 != '1' or pin !=1234):
    print("invalid credentials")
print("case 3 executes only if case 2 if block is false")
print()
print('test case 4 ')
pho_num = eval(input("Enter phone number: "))
if pho_num == '9912345678' or pho_num == 9912345678 or pho_num == '+91-9912345678' or pho_num == '+919912345678':
    print("The entered phone number is: ",pho_num)
print()
print('test case 5 ')
opt = input("Do you want to print the details - Y/N :")
if opt == 'y' or  opt == 'Y':
    print(f"username: {u1}\n phone number: {pho_num}")
print()
print('test case 1 with nested-if')
opt2 = input("Do you want to withdraw balance - Y/N :")
if opt2 == 'y' or  opt2 == 'Y':
    wb = int(input("Enter amount :"))
    if wb>balance:
        print('Insuffficient balance')
    if wb<balance:
        balance -= wb
        print("withdrawl amount :{} ".format(wb))
        print(f"Remaining balance {balance}")
print()
print("test case 6 if and nested if ")
opt5 = eval(input("sign in or sign up -> 1/2: "))
if(opt5 == 1):
    print("Enter id and password:")
if(opt5 == 2):
    em_name= input("Enter your name: ")
    em_dob = input("Enter date of birth: ")
    em_p1 = input("Enter password: ")
    em_cp1 = input("Enter Confirm password: ")
    if em_p1 == em_cp1:
        print("Account created : id == 100 && password:",em_p1)
        p = True
print('\ntest case 7 ')
em_id = int(input("Enter your id : "))
em_p2 = (input("Enter password: "))
p1 = '12345'
if (em_id == '100' and em_p2== p1 ) :
    print("Login success")
if (em_id != '100' or em_p1 != p1 ):
    print("Invalid credentials")
print()
print('test case 2  nested if')
opt3 = input("Do you want to change password -> Y/N:  ")
em_p1 = 'hello'
if opt3 == 'y' or opt3 == 'Y':
    p3 = input("Enter old password: ")
    print()
    if p == True:
        if em_p1 == p3:
            p2 = input("Enter new password: ")
            cp1 = input("Enter new password: ")
            if p2 == cp1:
                print("Passwords match, new password updated")
            if p2 != cp1:
                print("passwords do not match")
    if em_p2 == p3:
        p2 = input("Enter new password: ")
        cp1 = input("Enter new password: ")
        if p2 == cp1:
            print("Passwords match, new password updated")
        if p2 != cp1:
            print("passwords do not match")
print()
print("test case 8 ")
opt6 = input("Do you want to print the details - Y/N :")
if opt6 == 'y' or  opt6 =='Y':
    print("======Employee Details=====")
    print("ID = %s\nName = %s\nDOB=%s"%(em_id,em_name,em_dob))
print()
print('test case 9 ')
x2 = int(input("Enter a number : "))
if x2 <= 100:
    print("Below 100")
if x2 >= 100:
    print("more than 100")
print()
print('test case 10 ')
opt4 = input("choose sum/subtraction : S/D")
if opt4 == 's' or  opt4 =='S':
    print("sum = ",x1+x2)
if opt4 == 'd' or  opt4 =='D':
    print("The subtraction is : ",x1-x2)
print()
print('test case 11 ')
opt7 = input("Logout ? = Y/N")
if opt7 == 'y' or  opt7 == 'Y':
    print("Logout successful")
    l = True
if opt7 == 'n' or  opt7 =='N':
    print("Continue browsing")
    l = False
print()
print('test case 12 ')
l1 = eval(input("Enter a list:"))
for i in l1:
    if i<0:
        print("The number is neagtive: ",i)
    if i>0:
        print("the number is positive: ",i)
    if (i==0):
        print("the number is zero: ",i)
print()