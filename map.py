def test(i):
    return i*2
n = 1,4,3,2,5,2,15,6,21,1
t = 1,4,3,2,5,2,15,6,21,1
s = {4,92,10,3,10,20,10,3,14,5,2}
d = {1:23,45:5,3411:42,2:13}
if(__name__=="__main__"):
    
    l1 = list(map(test,n))
    print("list",l1)
    l2 = list(map(lambda x:x*5,n))
    print("Lambda",l2)

    t1 = tuple(map(test,t))
    print('tuple:',t1)
    t2 = tuple(map(lambda x:x*5,t))
    print("Lambda of tuple ",t2)

    s1 = set(map(test,s))
    print("set:",s1)
    s2 = set(map(lambda x:x*5,s))
    print("Lambda of set",s2)
'''d1 = dict(map(test,d.keys()))
    print("set:",d1)
    d2 = dict(map(lambda x:x*5,,d.keys()))
    print("Lambda of set",d2)'''
