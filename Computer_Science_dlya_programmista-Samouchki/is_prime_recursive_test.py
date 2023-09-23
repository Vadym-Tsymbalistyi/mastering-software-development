from unittest import TestCase, main
from Chapter_6_Math import is_prime_recursive


class IsPrimeRecursiveTest(TestCase):
    def test_True(self):

        self.assertTrue(is_prime_recursive(11))

    def test_False(self):

        self.assertFalse(is_prime_recursive(10))


if __name__ == '__main__':
    main()
