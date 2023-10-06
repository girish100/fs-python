def test(n):
    if n%2 == 0:
        return True
    else:
        return False
t = 1,4,3,2,5,2,15,6,21,1
s = {4,92,10,3,10,20,10,3,14,5,2}
d = {1:23,45:5,3411:42,2:13}
if(__name__=="__main__"):
    n = 1,4,3,2,5,2,15,6,21,1
    l1 = list(filter(test,n))
    print("list",l1)
    l2 = list(filter(lambda x:x%2 ==0,n))
    print("Lambda",l2)

    t1 = tuple(filter(test,t))
    print('tuple:',t1)
    t2 = tuple(filter(lambda x:x%2 ==0,t))
    print("Lambda of tuple ",t2)

    s1 = set(filter(test,s))
    print("set:",s1)
    s2 = set(filter(lambda x:x%2 ==0,s))
    print("Lambda of set",s2)
'''d1 = dict(filter(test,d.keys()))
    print("set:",d1)
    d2 = dict(filter(lambda x:x%2 ==0,d.keys()))
    print("Lambda of set",d2)
'''
    
