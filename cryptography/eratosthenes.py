import math

import numpy


def eratosthenes_sieve(n):
    """
    Simple, ancient algorithm for finding all prime numbers up to any given limit.
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    """

    if n > 1:
        sieve = numpy.zeros((n,), dtype=bool)
        sieve[0] = sieve[1] = True

        for i in range(2, int(math.sqrt(len(sieve))) + 1):
            if sieve[i] is True:
                continue

            for j in range(2 * i, len(sieve), i):
                sieve[j] = True

        return numpy.where(sieve == False)[0].tolist()

    else:
        raise ValueError("Upper bound has to be higher than 1")
