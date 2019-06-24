def getInput():
	print("Enter your mathematical expression:")
	expression = input() + "@"		# add '@' to end of expression to signify end of expression
	while(" " in expression):			# remove spaces from the inputted string
		expression = expression.replace(" ", "")
	return expression 
	
def getExpArray(expression):
	expArray = []
	opArray = ["*", "-", "+", "/", "(", ")"]
	curNum = ""

	for var in expression:
		if (var in opArray or var == "@"):
			if (len(curNum) > 0):
				expArray.append(float(curNum))
				curNum = ""
			if not(var == "@"):
				expArray.append(var)
		else:
			curNum = curNum + var

	return expArray

def eval(expArray):
	opArray = ["*", "-", "+", "/", "(", ")"]

	opStack = []
	valStack = []

	#print(expArray)

	for token in expArray:						# step 1
		if not(token in opArray):	
			valStack.append(token)
		elif (token == "("):
			opStack.append(token)
		elif (token == ")"):
			while(opStack[-1] != "("):
				operator = opStack.pop()
				n1 = valStack.pop()
				n2 = valStack.pop()

				valStack.append(basicEval(n1, n2, operator))
			opStack.pop()
		elif (token in opArray):								# operator that is not '(' or ')'
			while(len(opStack) > 0 and (precedence(opStack[-1]) >= precedence(token))):
				operator = opStack.pop()
				n1 = valStack.pop()
				n2 = valStack.pop()

				valStack.append(basicEval(n1, n2, operator))

			opStack.append(token)

		#print(valStack)
		#print(opStack)

	while(len(opStack) > 0):					# step 2
		operator = opStack.pop()
		n1 = valStack.pop()
		n2 = valStack.pop()

		valStack.append(basicEval(n1, n2, operator))

	if(len(valStack) == 1):					# step 3
		return valStack[0]
	else:
		return "error"

def precedence(op):  
  if op == "+" or op == "-": 
      return 1
  if op == "*" or op == "/": 
      return 2
  return 0


def basicEval(n1, n2, op):
	if(op == "+"):
		return (n2 + n1)
	elif(op == "-"):
		return (n2-n1)
	elif(op == "*"):
		return (n2*n1)
	elif(op == "/"):
		return (n2/n1)
	else:
		print("unknown operation")

def run():
	print("\n\n\n")
	expression = getInput()
	array = getExpArray(expression)
	result = eval(array)
	print(result)
	print("\n\n\n")

run()