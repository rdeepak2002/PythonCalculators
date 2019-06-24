def getInput():
	print("Enter your mathematical expression:")
	expression = input() + "@"		# add '@' to end of expression to signify end of expression
	
	return expression 
	
def getExpArray(expression):
	expArray = []
	opArray = ["*", "-", "+", "/"]
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
	while(len(expArray) > 1):
		index = -1

		if("*" in expArray):
			index = expArray.index("*")
			expArray[index] = expArray[index-1] * expArray[index+1]
		elif("/" in expArray):
			index = expArray.index("/")
			expArray[index] = expArray[index-1] / expArray[index+1]
		elif("+" in expArray):
			index = expArray.index("+")
			expArray[index] = expArray[index-1] + expArray[index+1]
		elif("-" in expArray):
			index = expArray.index("-")
			expArray[index] = expArray[index-1] - expArray[index+1]

		expArray.pop(index-1)
		expArray.pop(index)

	return expArray[0]


def run():
	expression = getInput()
	array = getExpArray(expression)
	result = eval(array)
	print(result)

run()