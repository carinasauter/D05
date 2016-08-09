#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body

user_name = input('What is your name?\n')


def infinite_stairway_room(count, user_name):
    print("{}, you walk through the door to see a dimly lit hallway." .format(user_name))
    print("At the end of the hallway is a", count *
          'long ', 'staircase going towards some light')
    next = input("What do you want to do, {}?" .format(user_name))

    # infinite stairs option
    if next == "take stairs":
        print('You take the stairs, {}' .format(user_name))
        if (count > 0):
            print("but you're not happy about it.")
            infinite_stairway_room(count + 1, user_name)
        else:
            print("... and you go down and down and down and finally open a door...")
            count += 1
            infinite_stairway_room(count, user_name)
    # option 2 == going back
    elif next in "turn around" or next in "go back":
        __main__()
    else:
        print("What do you want to do?")


def gold_room(user_name):
    print("This room is full of gold.  How much do you take, {}?" .format(user_name))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, {} learn to type a number." .format(user_name))

    if how_much < 50:
        print("Nice, you're not greedy, {}, you win!" .format(user_name))
        exit(0)
    else:
        dead("{}, you greedy goose!" .format(user_name))


def bear_room(user_name):
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear, {}?" .format(user_name))
    bear_moved = False

    while True:
        next = input("> ")

        if next in "take honey":
            dead("The bear looks at you, {}, then slaps your face off." .format(user_name))
        elif next == "taunt bear" or next == "taunt" and not bear_moved:
            print("The bear has moved from the door. You can go through it now, {}." .format(
                user_name))
            bear_moved = True
        elif next == "taunt bear" or next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews your leg off, {}." .format(user_name))
        elif next in "open door" and bear_moved:
            gold_room(user_name)
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu, {}." .format(user_name))
    print("He, it, whatever stares at you, {} and you go insane.".format(user_name))
    print("Do you flee for your life or eat your head, {}?" .format(user_name))

    next = input("> ")

    if "flee" in next:
        __main__()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(user_name)


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def __main__():
    # START the TextAdventure game
    count = 0
    print("{}, you are in a dark room." .format(user_name))
    print("There are three doors. Right, left, and straight.")
    print("Which one do you take, {}?" .format(user_name))

    next = input("> ")

    if next == "left":
        bear_room(user_name)
    elif next == "right":
        cthulhu_room(user_name)
    elif next == "straight":
        infinite_stairway_room(count, user_name)
    else:
        dead("You stumble around the room until you starve, {}." .format(user_name))

if __name__ == '__main__':
    __main__()
