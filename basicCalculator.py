print("\n\n\n")

print("Enter first number")

n1 = float(input())

print("Enter mathematical operation")

op = input()

print("Enter second number")

n2 = float(input())

print("Result:")

if(op == "+"):
	print(n1 + n2)
elif(op == "-"):
	print(n1-n2)
elif(op == "*"):
	print(n1*n2)
elif(op == "/"):
	print(n1/n2)
else:
	print("unknown operation")

print("\n\n\n")