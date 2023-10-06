f2 = [['a','b','c'],['d','e','f'],['g','h','i']]
f = [1,-1,-32]
print(f,'\n')
a = 0
b = 0
for j in f:
    if j<=a or j<=b:
        a = j
        b = j
for i in f:
    if i>a:
        b = a
        a = i
    if a>i and b<i:
        b = i
print("1st Largest: ",a)
print("2nd Largest: ",b)
print('\n',f2,'\n')
for x1 in f2:
    #print(x1)
    for y1 in x1:
        print(y1,end=' ')
    print()
print()
for x1 in range(1,11):
    for y1 in range(1,11):
        mul = x1*y1
        print('%d * %d = %d'%(x1,y1,mul))
    print()
