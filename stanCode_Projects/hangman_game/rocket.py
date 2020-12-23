"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 5


def main():
	"""

	the program will print a rocket which the size is determined by a constant"SIZE"
	"""
# 	head(SIZE)
# 	belt(SIZE)
# 	upper(SIZE)
# 	lower(SIZE)
# 	belt(SIZE)
# 	head(SIZE)
#
# def head(SIZE):
# 	"""
# 	:param SIZE: int
# 	:return: print the result
# 	"""
# 	for i in range(SIZE):
# 		for j in range(SIZE-i):
# 			print(' ', end='')
# 		for j in range(i+1):
# 			print('/', end='')
# 		for j in range(i+1):
# 			print('\\', end='')
# 		print('')
#
#
# def belt(SIZE):
# 	"""
# 	:param SIZE: int
# 	:return: print the result
# 	"""
# 	print('+', end='')
# 	for i in range(SIZE*2):
# 		print('=', end='')
# 	print('+', end='')
# 	print(' ')
#
#
# def upper(SIZE):
# 	"""
# 	:param SIZE: int
# 	:return: print the result
# 	"""
# 	for i in range(SIZE):
# 		print('|', end='')
# 		for j in range(SIZE-i-1):
# 			print('.', end='')
# 		for j in range(i+1):
# 			print('/\\', end='')
# 		for j in range(SIZE-i-1):
# 			print('.', end='')
# 		print('|', end='')
# 		print(' ')
#
#
# def lower(SIZE):
# 	"""
# 	:param SIZE: int
# 	:return: print the result
# 	"""
# 	for i in range(SIZE):
# 		print('|', end='')
# 		for j in range(i):
# 			print('.', end='')
# 		for j in range(SIZE-i):
# 			print('\\/', end='')
# 		for j in range(i):
# 			print('.', end='')
# 		print('|', end='')
# 		print(' ')




###### DO NOT EDIT CODE BELOW THIS LINE ######

	s = input('Please enter: ')
	name_diamond(s)

def name_diamond(s):

	for i in range(len(s)):
		print(s[0:1+i])
	for j in range(len(s)-1):
		for k in range(j+1):
			print('', end=" ")
		print(s[j+1:])


if __name__ == "__main__":
	main()