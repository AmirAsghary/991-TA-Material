from Assignments.Assignment1.Options.OptionA.main import A
from Assignments.Assignment1.Options.OptionA.simplified import ASimplified
from Assignments.Assignment1.Options.OptionC.main import C
from Assignments.Assignment1.Options.OptionC.simplified import CSimplified

# a Set of Menu Keys and Values
keys = {"main": "", "second": ""}


# Displays the Program's Main-Menu
def show_menu():
    print('\na) Single Numbers\t b) Two Numbers\t c) Three Numbers\t q) Exit')
    keys["main"] = input('Select One: ')

    # Quits the App.
    if keys["main"] == 'q':
        exit(1)

    return keys["main"]


# Sub-Menu A : Shows a List of Available Operations for a Single Number
def option_a():
    print('\nn) Num of Digits\t s) Sum of Digits\t f) Fibonacci\t p} IsPrime\t q) Exit')
    keys["second"] = input('Select One: ')

    # Sub-Menu A's Switch
    def a_switch(x):
        return {
            'n': A.digits_counter,
            's': A.digits_sum,
            'f': ASimplified.fibonacci_check,
            # 'f': A.fibonacci_check,
            'p': A.prime_check,
            'q': main_switch
        }[x]

    if keys["second"] != 'q':
        number = input('\nEnter a Number: ')
        a_switch(keys["second"])(int(number))
        option_a()
    else:
        main_switch(show_menu())()

    return keys["second"]


# Sub-Menu C : Shows a List of Available Operations for a Set of Three Numbers
def option_c():
    print('\np) GCD-Prime\t l) GCD-Fibonacci\t q) Exit')
    keys["second"] = input('Select One: ')

    # Sub-Menu C's Switch
    def c_switch(x):
        return {
            # 'p': C.gcd_prime,
            'p': CSimplified.gcd_prime,
            'l': C.gcd_fibonacci,
            'q': main_switch
        }[x]

    if keys["second"] != 'q':
        a = input('\nEnter the First Number: ')
        b = input('Enter the Second Number: ')
        c = input('Enter the Third Number: ')
        c_switch(keys["second"])(int(a), int(b), int(c))
        option_c()
    else:
        main_switch(show_menu())()

    return keys["second"]


# Emulates the Job of a Switch for the Main-Menu Options
def main_switch(x):
    return {
        'a': option_a,
        'c': option_c,
    }[x]


# The App's Starting Point.
main_switch(show_menu())()
