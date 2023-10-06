#bytes data type
l = {10,23,54,56,255}
b1 = bytes(l)

print(b1)
print(type(b1))
print()
print(*b1)
for x in b1:
    print(x)