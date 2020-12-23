"""
File: largest_digit.py
Name: Fenny
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the number to be compared
	:return: the largest digit in the number
	"""
	big = 0
	return find_largest_digit_helper(n, big)


def find_largest_digit_helper(n, big):
	"""
	:param n: the number to be compared
	:param big: the index to record the current largest digit in the number
	:return: the largest digit in the number
	"""
	if n > 0:
		if n < 10:
			if n > big:
				return n
			else:
				return big

		else:
			last_digit = n % 10
			new_num = n // 10
			if last_digit != 0:
				if last_digit > big:
					big = last_digit
					return find_largest_digit_helper(new_num, big)
				else:
					return find_largest_digit_helper(new_num, big)
	else:
		n = n * (-1)
		if n < 10:
			if n > big:
				return n
			else:
				return big

		else:
			last_digit = n % 10
			new_num = n // 10
			if last_digit != 0:
				if last_digit > big:
					big = last_digit
					return find_largest_digit_helper(new_num, big)
				else:
					return find_largest_digit_helper(new_num, big)


if __name__ == '__main__':
	main()
