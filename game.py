from words import words, en_words, de_words, en_words3_5, en_words6_8, en_words8_X, de_words3_5, de_words6_8, de_words8_X
from language import c, en, de
import time
import random
import sys,time
from os import system, name


de_words.extend(de_words3_5)            # Adding all the by length separated words to the main lists (IMPORTANT)
de_words.extend(de_words6_8)
de_words.extend(de_words8_X)

en_words.extend(en_words3_5)
en_words.extend(en_words6_8)
en_words.extend(en_words8_X)


def clear():                            # Clear Screen function for better overview in output
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_word():                         # Random word
    word = random.choice(words)
    return word.upper()


def play(word):                         # Play with word from above
    word_completion = "_" * len(word)
    show1 = "_ " * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    clear()
    lengthofword = len(word)
    print(c[4])
    print(lengthofword, c[5])
    print(display_hangman(tries))
    print(show1)
    print("\n")
    while not guessed and tries > 0:
        guess = input(c[6]).upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(c[7], guess)
            elif guess not in word:
                clear()
                print(guess, c[8])
                tries -= 1
                guessed_letters.append(guess)
                print(guessed_letters)
            else:
                clear()
                print(c[9], guess, c[10])
                guessed_letters.append(guess)
                print(guessed_letters)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(c[11], guess)
            elif guess != word:
                print(guess, c[12])
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print(c[13])
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        clear()
        print(c[14], word,"\n",tries, c[15])
        print(c[16])
        selection = input(c[2])
        if selection == "1":
            menu()
        if selection == "2":
            end_screen()
        if selection != "1" and selection != "2":
            menu()
    else:
        clear()
        print(c[17], word)
        print(c[16])
        selection = input(c[2])
        if selection == "1":
            menu()
        if selection == "2":
            end_screen()
        if selection != "1" and selection != "2":
            menu()


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def language_chooser():
    clear()
    print("Select a language from below:\n1. English\n2. German\n")
    language = input("Enter a number and press enter: ")
    if language == "1":
        c.extend(en)
        setlangen()
        menu()
    if language == "2":
        c.extend(de)
        setlangde()
        menu()

def end_screen():
    clear()
    print(c[3])

def info_screen():
    clear()
    print(c[18])
    f = open("lang.txt", "r")
    lan = f.read()
    if lan == "en":
        words.extend(en_words)
        wordcount = len(words)
        print(wordcount)
        words.clear()
    if lan == "de":
        words.extend(de_words)
        wordcount = len(words)
        print(wordcount)
        words.clear()
    sel = input(c[20])
    if sel != "~":
        menu()


def setlangen():
    f = open("lang.txt", "w")
    f.write("en")
    f.close()

def setlangde():
    f = open("lang.txt", "w")
    f.write("de")
    f.close()

def menu():
    clear()
    print(c[0])
    print(c[1])
    selection = input(c[2])
    if selection == "1":
        difficulty()
    if selection == "2":
        language_chooser()
    if selection == "3":
        info_screen()
    if selection == "4":
        end_screen()

def difficulty():
    clear()
    print(c[19])
    f = open("lang.txt", "r")
    lan = f.read()
    selection = input(c[2])
    if selection == "1":
        if lan == "en":
            words.clear()
            words.extend(en_words)
            main()
        if lan == "de":
            words.clear()
            words.extend(de_words)
            main()
    if selection == "2":
        if lan == "en":
            words.clear()
            words.extend(en_words3_5)
            main()
        if lan == "de":
            words.clear()
            words.extend(de_words3_5)
            main()
    if selection == "3":
        if lan == "en":
            words.clear()
            words.extend(en_words6_8)
            main()
        if lan == "de":
            words.clear()
            words.extend(de_words6_8)
            main()
    if selection == "4":
        if lan == "en":
            words.clear()
            words.extend(en_words8_X)
            main()
        if lan == "de":
            words.clear()
            words.extend(de_words8_X)
            main()

def main():
    word = get_word()
    play(word)



language_chooser()