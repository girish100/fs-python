def isEven(n):
	isEven = True
	print("function",isEven)
	for i in range(1, n+1):
		if isEven == True:
			isEven = False
		else:
			isEven = True

	return isEven

n = 11.5
# n = int(input("Enter a number"))
if isEven(n) == True:
	print ("Even")
else:
	print ("Odd")