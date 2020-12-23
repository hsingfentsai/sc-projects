"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    The program will let the user guess the random chosen word,
    if the user guesses wrong more than a specific of turns, the game will end
    """
    (bingo,dash,guess_word) = hide()  #hidden the random word
    guess(bingo, dash, guess_word)


def guess(bingo, dash, guess_word):
    """
    :param bingo: str, the random chosen word
    :param dash:  str, the hidden word
    :param guess_word: str, the alphabet that the user input
    :return:
    """
    ans = ''
    turn = N_TURNS

    while True:
        if turn >= 1:
            if guess_word.isalpha():
                if len(guess_word) > 1:
                    print('illegal format.')
                    guess_word = input('Your guess: ')
                else:
                    guess_word = guess_word.upper()
                    if guess_word in bingo:
                        for j in range(len(bingo)):
                            bingo_ch = bingo[j]
                            if bingo_ch == guess_word:
                                ans += guess_word
                            else:
                                if dash.find(bingo_ch) != -1:
                                    ans += bingo_ch
                                else:
                                    ans += '-'
                        dash = ans

                        if dash == bingo:
                            print('You are correct!\nYou win!')
                            print('The word was: ' + str(bingo))
                            turn = 0
                        else:
                            ans = ''
                            print('You are correct!')
                            print('The word looks like: ' + str(dash))
                            print('You have ' + str(turn) + ' guesses left.')
                            guess_word = input('Your guess: ')
                    else:
                        turn = turn - 1
                        print('There is no ' + str(guess_word) + '\'s in the word.')
                        if turn == 0:
                            print('End of the game\nThe answer is "' + str(bingo) + '"')
                            break
                        else:
                            print('The word looks like: ' + str(dash))
                            print('You have ' + str(turn) + ' guesses left.')
                            guess_word = input('Your guess: ')

            else:
                print('illegal format.')
                guess_word = input('Your guess: ')





def hide():
    """
    The function will hidden the random word into dash'-'
    :return: the random word
    """
    bingo = random_word()
    print(bingo)
    dash = ''
    for i in range(len(bingo)):
        dash += '-'
    print('The word looks like: '+ str(dash))
    print('You have ' + str(N_TURNS) + ' guesses left.')
    guess_word = input('Your guess: ')
    return bingo, dash, guess_word


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
