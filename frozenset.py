s1 = {'12','abc',100+12j,1256.657,12,13,14,15,16,chr(65)}
s2 = frozenset(s1)
print(s1,type(s1),"\n")
print(s2,type(s2),'\n')
s1.add(10)
s1.add(11.9)
s1.add('ad')
print("After adding elements: ",s1,type(s1))
s1.remove('ad')
print("After removing:",s1)
print("Set data type s1 is mutable")
print()
print("But a frozenset data type is immutable and in case of modifying the data after declaration, it results in an error")
s2[0] = '12.4'