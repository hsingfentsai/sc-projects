"""
File: anagram.py
Name: Fenny
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dic = []
final = []

def main():
    global final
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or ' + str(EXIT) + ' to quit)')
    while True:
        word = str(input('Find anagram for: '))
        if word == EXIT:
            break
        else:
            find_anagrams(word)
            print(len(final), 'anagrams: ', final)
            final = []


def read_dictionary():
    """
    the function will add the content in 'dictionary.txt' into a list called dic[]
    """
    global dic
    with open(FILE, 'r') as f:
        for line in f:
            word_list = line.split()
            word = word_list[0].strip()
            dic.append(word)


def find_anagrams(s):
    """
    :param s: str, word to be searched
    """
    find_anagrams_helper(s, [])


def find_anagrams_helper(s, current):
    """
    :param s: str, word to be searched
    :param current: list, the current sub-string
    """
    if len(current) == len(s):
        word = ''
        for index in current:
            word += s[index]
        if word in dic:
            if word not in final:
                final.append(word)
                print('Searching...')
                print('Found: ' + word)
    else:
        for i in range(len(s)):
            if i in current:
                pass
            else:
                current.append(i)
                find_anagrams_helper(s, current)
                current.pop()


def has_prefix(sub_s):
    """
    :param sub_s: str, the substring to be compared
    :return: boolean
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
