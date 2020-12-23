"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The program will match the DNA with the DNA-substring
    and find out the most similar DNA-substring in the DNA
    """
    long = input('Please give me a DNA sequence to search: ')
    short = input('What DNA sequence would you like to match? ')
    result = match(long, short)
    print ('The best match is: ' + str(result))


def match(long,short):
    """
    :param long: string, the dna that was input
    :param short: string, the dna substring to identify
    :return: string, the best substring match with the dna
    """
    long = long.upper()
    short = short.upper()
    if short in long:
        return short
    else:
        new = ''
        match = new
        count = 0
        min_match = len(short)

        for i in range(len(long)-len(short)):
            for j in range(len(short)):
                # long_sub_string =
                short_ch = short[j]
                long_string = long[i:i+len(short)]
                long_ch = long_string[j]
                if short_ch == long_ch:
                    new += short_ch
                else:
                    new += long_ch
                    count = count + 1
            if count <= min_match:
                match = new
                min_match = count
                new = ''
                count = 0
            else:
                new=''
                count = 0
        return match





###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
