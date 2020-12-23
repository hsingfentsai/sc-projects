"""
File: quadratic_solver.py
Name: Fenny
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	The program will calculate Quadratic Equation
	and tell the user how many roots are there
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	discriminant = calculate(a, b, c)

	if discriminant < 0:
		print('No real roots')
	elif discriminant == 0:
		equal = -b / (2*a)
		print('One root: '+str(equal))
	else:
		root = math.sqrt(discriminant)
		bigger1 = (-b+root) / (2*a)
		bigger2 = (-b-root) / (2*a)
		print('Two roots: ' + str(bigger1) + ' , ' + str(bigger2))


def calculate(a,b,c):
	"""
	:param a: the first number to be input
	:param b: the second number to be input
	:param c: the third number to be input
	:return: the result of the formula
	"""
	discriminant = b*b-4*a*c
	return discriminant



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
