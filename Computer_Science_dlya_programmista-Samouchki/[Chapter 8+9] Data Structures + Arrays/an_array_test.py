from unittest import TestCase, main
from Chapter_8_9_Data_Structures_Arrays import an_array


class AnArrayTest(TestCase):
    def test_an_erray(self):
        mas = [1, 2, 4, 24, 43, 4, 5, 6, 8, 8, 65, 765, 345]
        result = [1, 43, 5, 65, 765, 345, 2, 4, 24, 4, 6, 8, 8]
        self.assertEqual(an_array(mas), result)


if __name__ == '__main__':
    main()
