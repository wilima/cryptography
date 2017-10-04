def gcd(a, b):
    """
    Efficient method for computing the greatest common divisor (GCD) of two numbers, the largest number that divides both of them without leaving a remainder
    https://en.wikipedia.org/wiki/Euclidean_algorithm
    """

    while b != 0:
        tmp = b
        b = a % b
        a = tmp

    return a;
