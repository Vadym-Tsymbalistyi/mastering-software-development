from unittest import TestCase, main
from remove_duplicate_words import remove_duplicate_words


class TestRemoveDuplicateWords(TestCase):
    def test_remove_duplicate_words(self):
        original_sentence = "I am a self-taught programmer looking for a job as a programmer ."
        expected_result = "I am a self-taught programmer looking for job as "
        self.assertEqual(remove_duplicate_words(original_sentence), expected_result)

    def test_remove_dots(self):
        original_sentence = "hello word..."
        expected_result = remove_duplicate_words(original_sentence)
        self.assertEqual(expected_result, "hello word")


if __name__ == '__main__':
    main()
