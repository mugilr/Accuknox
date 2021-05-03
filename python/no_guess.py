#!/bin/python

import random

att_list = []
def show_score():
    if len(att_list) <= 0:
        print("no high score")
    else:
        print("current high score:"+format(min(att_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    wanna_play = input("play the guessing game? (Enter Y/N) ")
    # Where the show_score function USED to be
    att = 0
    show_score()
    while wanna_play.lower() == "y":
        try:
            guess = input("Guess a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("not in range")
            if int(guess) == random_number:
                print("Correct")
                att += 1
                att_list.append(att)
                print("you took {} attempts".format(att))
                play_again = input("play again? (Enter Y/N) ")
                att = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("bye")
                    break
            elif int(guess) > random_number:
                print("lower")
                att += 1
            elif int(guess) < random_number:
                print("higher")
                att += 1
        except ValueError as err:
            print("not a valid one")
            print("({})".format(err))
    else:
        print("nandri")
if __name__ == '__main__':
    start_game()
