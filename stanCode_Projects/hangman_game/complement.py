"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    the program will find out the complement of the dna
    that the user inputs(dna alphabet contains only A,T,C,G)
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    print('The complement of '+ dna +' is '+ build_complement(dna))


def build_complement(dna):
    """
    :param dna: string, the dna that was input
    :return: string, the complement of the user's dna
    """
    dna = dna.upper()
    result = ''
    for i in range(len(dna)):
        ch = dna[i]
        if ch == 'A':
            result += 'T'
        elif ch == 'T':
            result += 'A'
        elif ch == 'C':
            result += 'G'
        elif ch == 'G':
            result += 'C'
    return result








###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
