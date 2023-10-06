#1. write a python script to read the city from the keyboard and display output with it's city specilization
print("\t\t=====City Highlights=====")

city = input("Enter the city : ")
x = city.lower()

if x == 'hyderabad' or x == 'hyd':
    print(city," is famous for biryani and charminar")
elif x == 'banglore' or x== 'ban' :
    print(city," is famous for its plesant weather with greenary and IT companies")
elif x == 'chennai':
    print(city," is famous for its south indian dishes and kollywood")
elif x == 'mumbai'or x =='bom':
    print(city," is famous for beaches, buildings, bollywood and vada pav")
elif x == 'delhi' or x=='del':
    print(city," is famous for historical buildings such as red fort, qutub minar etc.")
elif x=='kolkata':
    print(city," is famous for howrah bridge, kali mandir, sea food")
else:
    print("City's data not present ")
print()


#2. Write a python script to read 3 ineger values from the keyboard and display maximum number and minimum number
print("\t\t=====MAX and MIN of 3 inegers=====")
a = int(input("Enter an integer 1:"))
b = int(input("Enter an integer 2:"))
c = int(input("Enter an integer 3:"))
print()
#max
if a >b and a >c:
    max_ = a
elif b>a and b>c:
    max_ = b
elif c>a and c>b:
    max_ = c
#min
if a <b and a <c:
    min_ = a
elif b<a and b<c:
    min_ = b
elif c<a and c<b:
    min_ = c
'''
f = int(input("Enter an initial value 1: "))
h = f
for i in range(2):
    g = int(input("Enter a value:"))
    if f >= g and g<=h:
        h = g
    elif f <= g:
        f = g
max1 = f
min1 = f
'''
print("Maximum of 3 integers is : ",max_)
print("Minimum of 3 integers is : ",min_)
print()

#3. Write a python script, enter marks of the students from the keyboard.
#Subjects are : python,advanced python,Django,JavaScript,SQL,FastAPI
#if 60<avg.marks<70 -- A grade , 50<avg.marks<60 -- B grade , 40<avg.marks<50 -- c grade, avg<40 -- Fail
# if subject marks less than 36 stop the program
print("\t\t====Student Report====")
x1 = int(input("Enter marks obtained in python          : "))
if x1>=36 and x1 <=100:
    x2 = int(input("Enter marks obtained in Advanced python : "))
    if x2>=36 and x2 <=100:
        x3 = int(input("Enter marks obtained in Django          : "))
        if x3>=36 and x3 <=100:
            x4 = int(input("Enter marks obtained in JavaScript      : "))
            if x4>= 36 and x4 <=100:
                x5 = int(input("Enter marks obtained in SQL             : "))
                if x5>=36 and x5 <=100:
                    x6 = int(input("Enter marks obtained in FastAPI         : "))
                    if x6>=36 and x5 <=100:
                        sum = x1+x2+x3+x4+x5+x6
                        avg = sum/6
                        if 60<avg<70:
                            print("Percentage: {}%\nGrade: A grade".format(avg))
                        elif 50<avg<60:
                            print("Percentage: {}%\nGrade: B grade".format(avg))
                        elif 40<avg<50:
                            print("Percentage: {}%\nGrade: C grade".format(avg))
                        elif avg<40:
                            print("Percentage: {}%\nGrade: F grage".format(avg))
                        elif avg>70:
                            print("Percentage: {}%\nGrade: O grade".format(avg))
                        print()
print("End of an application")