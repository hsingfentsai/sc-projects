"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    The program will encrypt the alphabet letters
    and decode the words that the user inputs
    """
    secret_no = int(input('Secret number: '))
    ciphered = str(input('What\"s the ciphered String? '))

    new_alphabet = shift(secret_no)
    deciphered(new_alphabet , ciphered)


def shift(secret_no):
    """
    :param secret_no: int, determine how will the alphabet letters be encrypt
    :return: str, encrypted alphabet letters
    """
    new_alphabet = ''
    front_section = ALPHABET[:26-secret_no]
    back = ALPHABET[26-secret_no:]
    new_alphabet += back+front_section
    return new_alphabet


def deciphered(new_alphabet, ciphered):
    """
    :param new_alphabet: str, the encrypted alphabet
    :param ciphered: str, the words to be decoded
    :return: str, the decoded words
    """
    ciphered = ciphered.upper()
    deciphered = ''
    for i in range(len(ciphered)):
        ciphered_ch = ciphered[i]
        if new_alphabet.find(ciphered_ch) == -1:
            deciphered += ciphered_ch
        else:
            for j in range(len(new_alphabet)):
                new_alphabet_ch = new_alphabet[j]
                if ciphered_ch == new_alphabet_ch:
                    deciphered += ALPHABET[j]
    print('The deciphered string is: ' + deciphered)


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
