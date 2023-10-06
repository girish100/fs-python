#write a python script to read 1 string from the keyboard and perform the following operations:
str1 = input("Enter a string: ")
print("The string is: ",str1)
print()
def reverse():
    str2 = ""
    for x1 in str1:
        str2 = x1+str2
    print("Reverse of the given string is: ",str2)
    return str2

def vowels():
    c1 = 0
    for x2 in str1:
        if x2 in ('AEIOUaeiou'):
            print("The vowel is :",x2)
            c1 += 1
    print("The total vowel count is: ",c1)

def consonants():
    c2=0
    for x3 in str1:
        if x3 not in ('AEIOUaeiou !@#$%^&*():",.`~₹¡™£§ˆ¶•̐°1234567890'):
            print("The consonants are: ",x3)
            c2 +=1
    print("The total consonants are: ",c2)

def palindrome():
    p1 = reverse()
    print("p1",p1)
    if p1 == str1:
        print("The given string %s is a palindrome: "%(str1))
    else:
        print("The given string {} is not a palindrome".format(str1))   

def duplicates():
    str2 = ''
    for x4 in str1:
        if x4 not in str2:
            str2 = str2 + x4 
    print("After removing the duplicaate values the string is : ",str2)    

if(__name__=="__main__"):
       reverse()
       print()
       vowels()
       print()
       consonants()
       print()
       palindrome()
       print()
       duplicates()
print("End of an application")