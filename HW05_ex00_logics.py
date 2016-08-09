#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    prompt = "Please provide a number to determine if it is even or odd: \n "
    user_input = int(input(prompt))
    try:
        if user_input % 2 == 0:
            print('Even')
        else:
            print('Odd')
    except:
        print('You were just supposed to enter an integer...')


def ten_by_ten():
    for number in range(1, 10):
        number = ' ' + str(number)
        print(number, end=" ")
    print("10")
    for tens in range(10, 100, 10):
        for ones in range(1, 11):
            print(tens + ones, end=' ')
        print()


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    user_input = 0
    count = 0
    sum_of_input = 0
    prompt = "Please provide the next number. Once you want the average, please write 'done'.\n"
    try:
        user_input = input(prompt)
        while str(user_input) != 'done':
            count += 1
            sum_of_input = sum_of_input + int(user_input)
            user_input = input(prompt)
        if count > 0:
            return (sum_of_input / count)
        else:
            print('You need to enter a number first')
            find_average()
    except:
        print("That was not a number! Please start again")
        find_average()


##############################################################################
def main():
    even_odd()
    ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
