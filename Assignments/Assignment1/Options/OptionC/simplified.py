from Assignments.Assignment1.Options.OptionC.main import C


# Appends the divisors of 'number' to the 'div_list' list.
def divs_lister(number, div_list):
    i = 1
    while i <= number:
        if number % i == 0:
            div_list.append(i)
        i = i + 1

    return 1


class CSimplified(C):

    # Accepts argument 'a','b','c' (int), prints a list of divisors of a & b that are relatively prime to 'c'
    # returns the list if it passes and returns -1 if it fails.
    # in this simplified method, i replaced the Filter function implementation with for loops.
    @staticmethod
    def gcd_prime(a, b, c):

        if a < 1 or b < 1 or c < 1:
            print('\nINCORRECT Values. Inputs should be Positive numbers!')
            return -1

        a_divisors = []
        b_divisors = []

        # fill each list with their respective number's divisors
        divs_lister(a, a_divisors)
        divs_lister(b, b_divisors)

        # remove duplicate elements
        for _div in a_divisors:
            if _div in b_divisors:
                b_divisors.remove(_div)

        divisors = []
        # fill the 'divisors' list with 'a_divisors' and 'b_divisors'
        divisors.extend(a_divisors)
        divisors.extend(b_divisors)

        filtered = []

        for item in divisors:
            if item == 1:
                continue

            div_divisors = []
            divs_lister(item, div_divisors)

            for _div in div_divisors:
                if (not _div == 1) and (c % _div == 0):
                    break
            # executing the block below, means that the flow of the for loop above was not interrupted.
            # meaning: the number 'item' is relatively prime to 'c' so we add it the the list 'filtered'
            else:
                filtered.append(item)

        if len(filtered) == 0:
            print('\nNone of the factors of', a, '&', b, 'are relatively prime to', c)
            # print('Factors of', a, '&', b, ':', divisors)
        else:
            print('\nFactors of', a, '&', b, 'that are relatively prime to', c, ':', filtered)

        return filtered
