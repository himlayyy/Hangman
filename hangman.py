#!usr/bin/env python
import random
import string
from words import words_list

def get_word():
    word = random.choice(words_list)
    while " " in word or "-" in word:
        word = random.choice(words_list)
    return word

def get_input():
    word = get_word().upper()
    letters = set(string.ascii_uppercase)
    guesses = 0
    guessed_letters = set()
    word_letters = set(word)
    for letter in word:
        print(" _ ", end = " ")
    won = False
    while guesses < 11:
        print(" ")
        if word_letters == guessed_letters:
            won = True
            break
        guess = input("What's your guess? ").upper()
        if guess in guessed_letters:
            print("You guessed that already!")
        elif guess in word:
            print("Correct!")
            guessed_letters.add(guess)
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end = " ")
                else:
                    print("_", end = " ")
        else:
            guesses += 1
            print(f"Wrong! {11 - guesses} lives left")

    for letter in word:
        print(letter, end=" ")
    return won


won = get_input()
if won is True:
    print("\nYou have won!")
else:
    print("\nYou lost :( ")


