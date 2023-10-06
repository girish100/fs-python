username = "1"
pass1 = "1"
tnx_id = (1,2,3,4,5,6)
enc_tnx_id = bytearray(tnx_id)
balance = 122000
u1 = input("enter username: ")
p1 = input("enter password: ")
pin = int(input("Enter pin: "))
if u1 == username and (p1 == pass1 or pin ==1234):
    print("Verified ")
    print("Balance: ",balance)
    v = True
else: 
    print("invalid credentials")
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
        wb = int(input("Enter balance to withdraw: "))
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
                          print("Withdrawl balance:%d"%wb)
                          balance -= wb
                          print("Remaining Balance: ",balance)
                     else:
                          print("Invalid id")
                else:
                     print("End of an application")
    else:
         print("End of an application")
