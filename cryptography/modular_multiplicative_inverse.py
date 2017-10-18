from cryptography import extended_gcd


def inverse(a, m):
    return (extended_gcd.extended_gcd(a, m)[1] % m + m) % m
