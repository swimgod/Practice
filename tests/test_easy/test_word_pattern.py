from unittest import TestCase

from src.easy.WordPattern import WordPattern


class TestWordPattern(TestCase):
    def test_case1(self):
        pattern = "abba"
        s = "dog cat cat dog"
        expected = True
        actual = WordPattern.wordPattern(pattern, s)
        self.assertEqual(expected, actual)

    def test_case2(self):
        pattern = "abba"
        s = "dog dog dog dog"
        expected = False
        actual = WordPattern.wordPattern(pattern, s)
        self.assertEqual(expected, actual)

