#chaining operator
#15 valid cases
#10 invalid cases
print("\n=======Chaining operator 15 valid cases=======")
a = 15
b = 19
c = 11
resl1 = a+b == b+c
resl2 = b-a != b-c
resl3 =((a if a<b<c else b) if b<c else c)
resl4 = (a + b + c)*10
resl5 = a==b & b==c
print("case 1: ",resl1)
print("case 2: ",resl2)
print("case 3:",resl3)
print("case 4:",resl4)
print("case 5:",resl5)
str1 = 'hello' #input("enter a string: ")
str2 = 'there'#input("enter a string: ")
if str1 == str2 and len(str1) ==len(str2):
    print("case 6:",str1,"",str2)
else:
    print("case 6:",str1,"",str2)
resl6 = len(str1) & len(str2) & a & c
print("case 7:",resl6)
resl7 = (len(str1) ^ len(str2)) & (a ^ c)
print("case 8:",resl7)
d = 9
e = 1
print(a,b,c,d,e)
min_ = a if a<b<c<d<e else b if b<c<d<e else c if c<d<e else d if d<e else e
print("case 9 min : ",min_)
max_ = a if a>b>c>d>e else b if b>c>d>e else c if c>d>e else d if d>e else e
print("case 10 max: ",max_)
