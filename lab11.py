#1. Write a python script with all posibilities can we read the data using lambda keyword
#lambda used for implementing nameless function
s1 = lambda str1:str1
s2 = lambda str2:input("Enter another string: ")

print(s1(str1=input("Enter a string: ")))
print(s2(str2=''))
print()
#2. write a python script can we use lambda inside a function
print("Using lambda keyword inside a function: ")
def lambda1():
    s2 = lambda x1:x1+5
    s3 = lambda str3:5
    print(s3(str3=''))
    print(s2(7))
lambda1()
print()
#3.write a python script to know the difference b/w namefull and nameless function
def namefull(a,b):
    sum = a+b
    print("the sum from namefull function is: ",sum)

nameless = lambda a,b:a+b
a = 5
b = 10
namefull(a,b)
print()
print("The sum from nameless func is: ",nameless(a,b))
print()
#4. write a python script develop all the assignment operators with lambda keyword
c = 12
d = 14
sum = lambda c,d:c + 1 
# +=,-=,*= etc not supported because lambda takes expression as input and assignment operator is a statement
