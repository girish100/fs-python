import random as r
print(r.random()) # returns a value in between 0.0 to 1.1
print(r.randint(3,10)) #returns a random int value in specified range (begin,end) end = end 
print(r.randrange(15)) #returns a random value until the given range
print(r.uniform(3,17)) #returns a random float value in specified range 
t1 = [chr(29),chr(36),chr(88),chr(128)]
print(r.choice(t1)) # returns a random coice from given group of elements
for i in range(33,126):
    print("chr({})".format(i),end=',')