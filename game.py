from words import words, en_words, de_words
from language import c, en, de
import time
import random
import sys,time
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_word():
    word = random.choice(words)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    clear()
    lengthofword = len(word)
    print(c[4])
    print(lengthofword, c[5])
    print(display_hangman(tries))
    print(word_completion)
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
        words.extend(en_words)
        menu()
    if language == "2":
        c.extend(de)
        words.extend(de_words)
        menu()

def end_screen():
    clear()
    print(c[3])

def info_screen():
    clear()
    print(c[18])
    wordcount = len(words)
    print(wordcount)

def menu():
    clear()
    print(c[0])
    print(c[1])
    selection = input(c[2])
    if selection == "1":
        main()
    if selection == "2":
        language_chooser()
    if selection == "3":
        info_screen()
    if selection == "4":
        end_screen()

def main():
    word = get_word()
    play(word)



language_chooser()