import unittest

from cryptography import eratosthenes, euler, extended_gcd, factorization, gcd

from .context import cryptography


class GcdTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_gcd(self):
        self.assertEqual(
            gcd.gcd(1071, 462),
            21)

    def test_gcd2(self):
        self.assertEqual(
            gcd.gcd(270, 192),
            6)


class ExtendedGcdTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_extended_gcd(self):
        self.assertEqual(
            extended_gcd.extended_gcd(1914, 899),
            (29, 8, -17))


class FactorizationTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_factorization(self):
        self.assertEqual(
            factorization.integer_factorization(315),
            [3, 3, 5, 7])


class EratosthenesTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_eratosthenes_sieve(self):
        self.assertEqual(
            eratosthenes.eratosthenes_sieve(20),
            [2, 3, 5, 7, 11, 13, 17, 19])


class EulerFunctionTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_euler_function(self):
        self.assertEqual(
            euler.euler_function(1),
            1)

    def test_euler_function(self):
        self.assertEqual(
            euler.euler_function(5),
            4)


if __name__ == '__main__':
    unittest.main()
