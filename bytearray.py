print()
l2 = 10,11,3,65,78,19,20
print(l2, type(l2))
print()
ba1 = bytearray(l2)
print(ba1, type(ba1))
print()
print(*ba1)
print()
for y in ba1:
    print(y)
print()
print("=====Modifying the bytes array ======")
ba1[0] = 25
ba1[1] = 74
ba1[2] = 177
ba1[3] = 206
ba1[4] = 212
ba1[5] = 250
print(ba1)
print(type(ba1))
print(*ba1)
print()
print("end of code")