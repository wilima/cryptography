from cryptography import factorization


def euler_function(n):
    """
    Euler's totient function counts the positive integers up to a given integer n that are relatively prime to n
    https://www.algoritmy.net/article/57/Eulerova-veta
    """

    if n == 1:
        return 1

    if n > 1:
        result = n
        prime_factors = factorization.integer_factorization(n)

        for factor in prime_factors:
            result = result * (1 - 1 / factor)

        return int(result)
    else:
        raise ValueError("Argument n has to be higher than 1")
