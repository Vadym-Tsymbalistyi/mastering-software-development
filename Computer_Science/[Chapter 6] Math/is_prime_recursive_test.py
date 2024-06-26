from unittest import TestCase, main
from is_prime_recursive import is_prime_recursive


class IsPrimeRecursiveTest(TestCase):
    def test_True(self):
        self.assertTrue(is_prime_recursive(11))

    def test_False(self):
        self.assertFalse(is_prime_recursive(10))

    def test_False2(self):
        self.assertFalse(is_prime_recursive(1))


if __name__ == '__main__':
    main()
