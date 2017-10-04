import math


def integer_factorization(n):
    """
    The algorithm takes as its inputs n, the integer to be prime factored
    http://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
    """

    result = []

    while n % 2 == 0:
        result.append(2)
        n = n / 2

    end = int(math.sqrt(n)) + 1

    for i in range(3, end, 2):
        while n % i == 0:
            result.append(i)
            n = n / i

    if n > 2:
        result.append(n)

    return result
