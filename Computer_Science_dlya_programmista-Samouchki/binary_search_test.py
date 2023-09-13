from unittest import TestCase, main
from Chapter_3_Search_Algorithms import binary_search


class BinarySearchTest(TestCase):
    def test_True(self):
        a_list = ['apple', 'banana', 'kiwi', 'orange', 'plum']
        n = 'banana'
        result = binary_search(a_list, n)
        self.assertTrue(result)

    def test_False(self):
        a_list = ['apple', 'banana', 'kiwi', 'orange', 'plum']
        n = 'mango'
        result = binary_search(a_list, n)
        self.assertFalse(result)


if __name__ == '__main__':
    main()
