print('case 1') 
#nested forloop and for with else block
L1=[101,102,103,104,105,106,107,900,1,2,3,4,5,6,7]
for x1 in L1:
    if(x1>899):
        print("Welcome to IHUB_APP_STORE ...")
        break 
    print("IHUB PROCESSING ITEMS ARE:",x1)
else:
    print('All Iterations are done successfully ....')
print()
print('case 2')
for x2 in range(10,15):
    print(x2+1)
print('case 3')
