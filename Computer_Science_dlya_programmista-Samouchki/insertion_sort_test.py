from unittest import TestCase, main
from Chapter_4_Sorting_Algorithms import insertion_sort


class InsertionSortTest(TestCase):
    def test_insertion_sort(self):
        a_list = [3, 2, 4, 567, 7, 8, 7, 445, 34]
        result = [2, 3, 4, 7, 7, 8, 34, 445, 567]
        self.assertEquals(insertion_sort(a_list), result)


if __name__ == '__main__':
    main()
