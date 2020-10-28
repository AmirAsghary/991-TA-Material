from Assignments.Assignment1.Options.OptionA.main import A


class ASimplified(A):

    # Accepts argument 'number' (int), checks if 'number' is part of the Fibonacci Sequence.
    # returns the position if 'number' passes and returns -1 if it fails.
    # in this simplified method, i de-coupled the variable 'i' and the fibonacci numbers to avoid using sets and dicts
    @staticmethod
    def fibonacci_check(number):

        if number < 0:
            print('\033[91m\nINCORRECT Value. Input should be a Positive numbers!\033[0m')
            return -1

        c = 0
        a = 1
        b = 1
        if number == c:
            print(number, 'is the first member of the Fibonacci Sequence.')
            return 1
        if number == a:
            print(number, 'is the second and the third member of the Fibonacci Sequence.')
            return [2, 3]

        c = b
        i = 2
        while c < number:
            c = a + b
            i += 1
            b = a
            a = c
        if c == number:
            print(number, 'is the', i, 'th', 'member of the Fibonacci Sequence.')
            return i
        else:
            print(number, 'is NOT a Fibonacci number.')
            return -1
