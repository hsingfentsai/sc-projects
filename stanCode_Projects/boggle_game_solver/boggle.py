"""
File: boggle.py
Name: Fenny
----------------------------------------
TODO: User will input 4 rows of words and the program will attempt to find words in sequences of adjacent letters.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
dic = []
final = []

def main():
	"""
	the program will check whether the words which user input is legal
	and will use recursion to find words in sequences of adjacent letters.
	"""
	read_dictionary()
	direction = [(0,0), (0,1), (0,2), (0,3), (1,0), (1,1), (1,2), (1,3),(2,0), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3)]
	lst = []
	first_lst = []
	first = input('1 row of letter: ')
	first = first.lower()
	first = first.split(' ')
	if len(first) < 4 or len(first) > 5:
		print('Illegal input')
	else:
		for word in first:
			first_lst.append(word)
			lst.append(word)
		if len(first_lst[0]) > 1 or len(first_lst[1]) > 1 or len(first_lst[2]) > 1 or len(first_lst[3]) > 1\
				or first_lst[0] not in ALPHABET or first_lst[1] not in ALPHABET or first_lst[2] not in ALPHABET or first_lst[3] not in ALPHABET:
			print('Illegal input')
		else:
			second_lst = []
			second = str(input('2 row of letter: '))
			second = second.lower()
			second = second.split(' ')
			if len(second) < 4 or len(second) > 5:
				print('Illegal input')
			else:
				for word in second:
					second_lst.append(word)
					lst.append(word)
				if len(second_lst[0]) > 1 or len(second_lst[1]) > 1 or len(second_lst[2]) > 1 or len(second_lst[3]) > 1\
						or second_lst[0] not in ALPHABET or second_lst[1] not in ALPHABET or second_lst[2] not in ALPHABET or second_lst[3] not in ALPHABET:
					print('Illegal input')
				else:
					third_lst = []
					third = str(input('3 row of letter: '))
					third = third.lower()
					third = third.split(' ')
					if len(third) < 4 or len(third) > 5:
						print('Illegal input')
					else:
						for word in third:
							third_lst.append(word)
							lst.append(word)
						if len(third_lst[0]) > 1 or len(third_lst[1]) > 1 or len(third_lst[2]) > 1 or len(third_lst[3]) > 1\
								or third_lst[0] not in ALPHABET or third_lst[1] not in ALPHABET or third_lst[2] not in ALPHABET or third_lst[3] not in ALPHABET:
							print('Illegal input')
						else:
							fourth_lst = []
							fourth = str(input('4 row of letter: '))
							fourth = fourth.lower()
							fourth = fourth.split(' ')
							if len(fourth) < 4 or len(fourth) > 5:
								print('Illegal input')
							else:
								for word in fourth:
									fourth_lst.append(word)
									lst.append(word)
								if len(fourth_lst[0]) > 1 or len(fourth_lst[1]) > 1 or len(fourth_lst[2]) > 1 or len(fourth_lst[3]) > 1\
										or fourth_lst[0] not in ALPHABET or fourth_lst[1] not in ALPHABET or fourth_lst[2] not in ALPHABET or fourth_lst[3] not in ALPHABET:
									print('Illegal input')
								else:
									find_word(lst, direction)
									print('There are ' + str(len(final)) + ' words in total.')


def find_word(lst, direction):
	"""
	:param lst: lst, words that user input
	:param direction: lst, the index(x,y) of each item in lst
	"""
	word = ''
	find_index = []
	current = []
	find_word_helper(lst, direction, word, find_index, current)


def find_word_helper(lst, direction, word, find_index, current):
	"""
	:param lst, words that user input
	:param direction: lst, the index(x,y) of each item in lst
	:param word: str, the word to be searched in the dictionary
	:param find_index: int, index that have already been found
	:param current: lst, index(x,y) of the words to be string
	"""
	if not has_prefix(word):
		return
	else:
		if len(word) >= 4 and word not in final and word in dic:
			final.append(word)
			print('Found: ' + word)
		for i in range(len(lst)):
			if i in find_index:
				continue
			elif len(current) > 0:
				if direction[i][0] < current[(len(current)-1)][0]-1 or direction[i][0] > current[(len(current)-1)][0]+1:
					continue
				if direction[i][1] < current[(len(current)-1)][1]-1 or direction[i][1] > current[(len(current)-1)][1]+1:
					continue
			current.append(direction[i])
			find_index.append(i)
			find_word_helper(lst, direction, word+lst[i], find_index, current)
			current.pop()
			find_index.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""

	global dic
	with open(FILE, 'r') as f:
		for line in f:
			word_list = line.split()
			word = word_list[0].strip()
			dic.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
