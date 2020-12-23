"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
STOP = -100

def main():
	"""
	The program will print out the highest temperature, the lowest temperature and the average temperature.
	Also, it will print out how many cold days are there.
	"""
	print('stanCode \"Weather Master 4.0\"! ')
	data = int(input('Next Temperature: (or ' + str(STOP) + ' to quit)? '))
	if data == STOP:
		print('No temperatures were entered.')
	else:
		max = data
		min = data
		total = data
		count = 1 	#to record how many pieces of data have been entered
		coldday = 0		#to record how many days of cold days(temperature < 16)

		if data < 16:	#to identify whether the first input temperature is a cold day
			coldday += 1

		while True:
			temp = int(input('Next Temperature: (or ' + str(STOP) + ' to quit)? '))
			if temp == STOP:
				break
			elif temp > max:
				max = temp
			elif temp < min:
				min = temp

			if temp < 16:
				coldday += 1
			total = sum(total, temp)
			count += 1
		average = total / count

		print('Highest temperature: ' + str(max))
		print('Lowest temperature: ' + str(min))
		print('Average: ' + str(average))
		print(str(coldday) + ' cold day(s)')


def sum(total,temp):
	"""
	:param total: the total amount of previously input temperatures
	:param temp: the temperature that the user input
	:return: total plus temp
	"""
	sum = total + temp
	return sum







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
