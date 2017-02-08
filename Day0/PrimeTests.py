# Author Paul Upendo
# TestCases for my prime number generator.
import unittest

import prime


class PrimeTests(unittest.TestCase):

    def test_output_prime(self):  # To test if output is prime.
        self.assertEqual(prime.primes(5), [2, 3])

    def test_positive(self):  # To ensure that negative input raises a ValueError.
        with self.assertRaises(ValueError):
            prime.primes(-2)

    def test_not_string(self):  # To test and ensure string inputs raise a TypeError.
        with self.assertRaises(TypeError):
            prime.primes('kama')

    def test_not_zero(self):  # To test and see that user input should not be zero.
        with self.assertRaises(ValueError):
            prime.primes(0)

    def test_not_float(self):  # To ensure float types raise a ValueError.
        with self.assertRaises(TypeError):
            prime.primes(2.0)

    def test_one_prime(self):  # To ensure that the output does not include 1.
        self.assertNotIn(1, prime.primes(10))

    def test_zero_prime(self):  # To ensure that the output does not include 0.
        self.assertNotIn(0, prime.primes(10))

    def test_one(self):  # To ensure that the output for one is an empty list.
        self.assertEqual(prime.primes(1), [])

    def test_not_even(self):
        self.assertNotEqual(prime.primes(10), [2, 4, 6, 8])  # To ensure that output is not a series of even numbers.

    def test_not_odd(self):
        self.assertNotEqual(prime.primes(10), [3, 5, 7, 9])  # To ensure output is not a series of odd numbers.


if __name__ == '__main__':
    unittest.main()
