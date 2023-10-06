#command line argument <argv>
# execute as ----> python3 cla.py 10 20 30 40 50 ....
from sys import *
print(argv)
print(type(argv))
print('string concatenation:',(argv[0])+(argv[1]))
print("Reading values from 'argv' list:")
for i in argv:
    print(i)
print('Two elements int addition: ',int(argv[2])+int(argv[1]))
b = 0
for i in argv[1:]:
    b = b + int(i)
print("Addition: ",b)