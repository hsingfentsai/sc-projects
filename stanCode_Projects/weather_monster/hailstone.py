"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program will break down the number which was input by the user to 1
    and record how many steps it needs to reach 1
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    count = 0
    if n == 1:
        print('It took 0 steps to reach 1')
    else:
        while True:
            if n == 1:
                print('It took ' + str(count) + ' steps to reach 1')
                break
            elif n % 2 == 1:
                next_n = 3*n+1
                print(str(n)+' is odd, so I make 3n+1: '+ str(next_n))
                n = next_n
                count += 1  #to record how many times it took to reach 1

            elif n % 2 == 0:
                next_n =int(n/2)
                print(str(n) + ' is even, so I take half: ' + str(next_n))
                n = next_n
                count += 1  #to record how many times it took to reach 1



            ###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
