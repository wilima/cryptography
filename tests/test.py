import unittest

from cryptography import (eratosthenes, euler, extended_gcd, factorization,
                          gcd, modular_multiplicative_inverse)
from cryptography.ciphers import affine, shift, substitution, vigener

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


class ModularInverseTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_modular_inverse(self):
        self.assertEqual(
            modular_multiplicative_inverse.inverse(5, 26),
            21)


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

    def test_euler_function2(self):
        self.assertEqual(
            euler.euler_function(5),
            4)


class ShiftCipherFunctionTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_shift_encrypt_function(self):
        self.assertEqual(
            shift.encrypt('BARBARIUTOCI', 3),
            'eduedulxwrfl'.upper())

    def test_shift_decrypt_function(self):
        self.assertEqual(
            shift.decrypt('eduedulxwrfl', 3),
            'BARBARIUTOCI')

    def test_shift_crack_function(self):
        self.assertEqual(
            'BARBARIUTOCI' in shift.crack('eduedulxwrfl', 26),
            True)

class AffineCipherFunctionTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_affine_encrypt_function(self):
        self.assertEqual(
            affine.encrypt('THEINITIAL', (5, 9)),
            'ASDXWXAXJM')

    def test_affine_decrypt_function(self):
        self.assertEqual(
            affine.decrypt('ASDXWXAXJM', (5, 9)),
            'THEINITIAL')

    def test_affine_crack_function(self):
        self.assertEqual(
            'THEINITIAL' in affine.crack('ASDXWXAXJM', 26),
            True)


class SubstitutionCipherFunctionTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_substitution_encrypt_function(self):
        self.assertEqual(
            substitution.encrypt('FLEEATONCEWEAREDISCOVERED', ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZEBRASCDFGHIJKLMNOPQTUVWXY')),
            'SIAAZQLKBAVAZOARFPBLUAOAR')

    def test_substitution_decrypt_function(self):
        self.assertEqual(
            substitution.decrypt('SIAAZQLKBAVAZOARFPBLUAOAR', ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ZEBRASCDFGHIJKLMNOPQTUVWXY')),
            'FLEEATONCEWEAREDISCOVERED')


class VigenerCipherFunctionTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_vigener_encrypt_function(self):
        self.assertEqual(
            vigener.encrypt('KULTURNIATASEJESPION', 'PES'),
            'ZYDIYJCMSIEKTNWHTADR')

    def test_vigener_decrypt_function(self):
        self.assertEqual(
            vigener.decrypt('ZYDIYJCMSIEKTNWHTADR', 'PES'),
            'KULTURNIATASEJESPION')



if __name__ == '__main__':
    unittest.main()
