from functools import reduce


# Appends the divisors of 'number' to the 'div_list' list.
def divs_lister(number, div_list):
    i = 1
    while i <= number / 2:
        if number % i == 0:
            div_list.append(i)
        i = i + 1
    else:
        div_list.append(number)
    # div_list = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) #really fast!
    return 1


class C:

    # Accepts argument 'a','b','c' (int), prints a list of divisors of a & b that are relatively prime to 'c'
    # returns the list if it passes and returns -1 if it fails.
    @staticmethod
    def gcd_prime(a, b, c):

        def filter_divisors(third_number):
            def _filter(div):
                if third_number % div == 0:
                    return False
                return True
            return _filter

        if a < 1 or b < 1 or c < 1:
            print('\033[91m\nINCORRECT Values. Inputs should be Positive numbers!\033[0m')
            return -1

        divisors = []

        divs_lister(a, divisors)
        divs_lister(b, divisors)

        divisors = list(set(divisors))

        _div_filter = filter_divisors(c)
        filtered = []
        for item in divisors:
            div_divisors = []
            divs_lister(item, div_divisors)
            filtered.extend(filter(_div_filter, div_divisors))

        filtered = set(filtered)
        if len(filtered) == 0:
            print('\nNone of the factors of', a, '&', b, 'are relatively prime to', c)
            # print('Factors of', a, '&', b, ':', divisors)
        else:
            print('\nFactors of', a, '&', b, 'that are relatively prime to', c, ':', filtered)

        return filtered

    # Accepts arguments 'a','b','c'(int),prints a list of Fibonacci numbers between a&b that are relatively prime to 'c'
    # returns the list if it passes and returns -1 if it fails.
    @staticmethod
    def gcd_fibonacci(a, b, c):

        def filter_divisors(third_number):
            def _filter(div):
                div_divisors = []
                divs_lister(div, div_divisors)
                for div in div_divisors:
                    if third_number % div == 0 and not div == 1:
                        return False
                return True

            return _filter

        if a < 1 or b < 1 or c < 1:
            print('\033[91m\nINCORRECT Values. Inputs should be Positive numbers!\033[0m')
            return -1

        fibs = []

        x = 0
        y = 1
        z = 1

        while z < a:
            x = y
            y = z
            z = x + y

        while z < b:
            fibs.append(z)
            x = y
            y = z
            z = x + y

        print(fibs)

        _div_filter = filter_divisors(c)

        filtered = []

        filtered.extend(filter(_div_filter, fibs))

        print(filtered)

        if len(filtered) == 0:
            print('\nNo Fibonacci number exists between', a, '&', b, 'that are relatively prime to', c)
        else:
            print('\nFibonacci numbers between', a, '&', b, 'that are relatively prime to', c, ':', filtered)

        return filtered
