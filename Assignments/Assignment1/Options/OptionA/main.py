import math


class A:

    # Accepts argument 'number' (int), prints and returns the amount of digits of 'number'.
    @staticmethod
    def digits_counter(number):
        count = 0
        _number = math.fabs(number)
        while _number > 0:
            count = count + 1
            _number = _number // 10

        print(number, 'has', count, 'digits.')
        return count
        # return int(math.log10(_number)) + 1
        # return len(str(_number))

    # Accepts argument 'number' (int), prints and returns the sum of digits of 'number'.
    @staticmethod
    def digits_sum(number):
        _sum = 0
        _number = math.fabs(number)
        while _number != 0:
            _sum = _sum + (_number % 10)
            _number = _number // 10

        print('the Sum of Digits of ', number, 'is equal to ', int(_sum))
        return sum

    # Accepts argument 'number' (int), checks if 'number' is part of the Fibonacci Sequence.
    # returns dict : {'value': x, 'nth': i} if 'number' passes and returns -1 if it fails.
    @staticmethod
    def fibonacci_check(number):

        if number < 0:
            print('\033[91m\nINCORRECT Value. Input should be a Positive numbers!\033[0m')
            return -1

        c = {'value': 0, 'nth': 1}
        a = {'value': 1, 'nth': 2}
        b = {'value': 1, 'nth': 3}
        if number == c['value']:
            print(number, 'is the', str(c['nth']) + 'st', 'member of the Fibonacci Sequence.')
            return c
        if number == a['value']:
            print(number, 'is the', str(a['nth']) + 'nd', 'and', str(b['nth']) + 'rd',
                  'member of the Fibonacci Sequence.')
            return {"a": a, "b": b}

        c['nth'] = b['nth']
        while c['value'] < number:
            c['value'] = a['value'] + b['value']
            c['nth'] += 1
            b['value'] = a['value']
            a['value'] = c['value']
        if c['value'] == number:
            print(number, 'is the', str(c['nth']) + 'th', 'member of the Fibonacci Sequence.')
            return c
        else:
            print(number, 'is NOT a Fibonacci number.')
            return -1

    # Accepts argument 'number' (int), checks whether 'number' is prime or not.
    # returns 1 if it passes and returns -1 if it fails.
    @staticmethod
    def prime_check(number):

        if number < 0:
            print('\033[91m\nINCORRECT Value. Input should be a Positive numbers!\033[0m')
            return -1

        if number == 0:
            print('0 is not a Prime number.')
            return -1

        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a Prime number.")
                return -1
        else:
            print(number, "is a Prime number.")
            return 1
