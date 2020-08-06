def arithmetic_arranger(problems, showResults=False):
	arranged_problems = ""
	marksOfEquations = ["+", "-"]
	finalConfig = []
	for equation in problems:
		for mark in marksOfEquations:
			for things in equation:
				if things == "*" or things == "/":
					return "Error: Operator must be '+' or '-'."
				if mark == things:
					# print(equation)
					splitEquation = equation.split(mark)
					for number in splitEquation:
						try:
							if int(number) > 9999:
								return "Error: Numbers cannot be more than four digits."
							splitEquation[splitEquation.index(number)] = int(number)
						except ValueError:
							return "Error: Numbers must only contain digits."
					splitEquation.append(mark)
					finalConfig.append(splitEquation)


	if len(finalConfig) > 5:
		return 'Error: Too many problems.' 


	# First Line
	for equ in finalConfig:
		# print(equ)
		length = 5
		coeffecient = max(len(str((equ[0]))), len(str(equ[1])))+2
		# print(equ, coeffecient)
		if (equ != finalConfig[-1]):
			arranged_problems += f"%{coeffecient}d    " % equ[0]
		else:
			arranged_problems += f"%{coeffecient}d" % equ[0]

	arranged_problems += '\n'
	# Second Line
	for equ in finalConfig:
		coeffecient = max(len(str((equ[0]))), len(str(equ[1])))+1
		if (equ != finalConfig[-1]):
			arranged_problems += f"%s%{coeffecient}d    " % (equ[2], equ[1])
		else:
			arranged_problems += f"%s%{coeffecient}d" % (equ[2], equ[1])

	# Dashes Line
	arranged_problems += '\n'
	for dashToBe in finalConfig:
		coeffecient = max(len(str((dashToBe[0]))), len(str(dashToBe[1])))

		for dash in range(coeffecient+2):
			arranged_problems += '-'
		if ( dashToBe != finalConfig[-1]):
			arranged_problems += '    '

	# Results
	if(showResults):
		arranged_problems += '\n'
		results = 0
		for equ in finalConfig:
			if equ[2] == '+':
				results = equ[0] + equ[1]
			if equ[2] == '-':
				results = equ[0] - equ[1]


			coeffecient = max(len(str((equ[0]))), len(str(equ[1])))+1
			if (equ != finalConfig[-1]):
				arranged_problems += f"%{coeffecient+1}d    " % results
			else:
				arranged_problems += f"%{coeffecient+1}d" % results

	return arranged_problems