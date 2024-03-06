from unittest import TestCase, main
from filter_words import filter_words


class FilterWordsTest(TestCase):
    def test_filter_words(self):
        list1 = ["selftaught", "code", "sit", "eat", "programming", "dinner", "one", "two", "coding", "a", "tech"]
        result = ['selftaught', 'programming', 'dinner', 'coding']
        self.assertEqual(filter_words(list1), result)


if __name__ == '__main__':
    main()
