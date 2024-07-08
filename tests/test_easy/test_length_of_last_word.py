from unittest import TestCase

from src.easy.LengthOfLastWord import LengthOfLastWord


class TestLengthOfLastWord(TestCase):
    def test_case_1(self):
        s = "Hello World"
        expected = 5
        actual = LengthOfLastWord.lengthOfLastWord(s)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        s = "   fly me   to   the moon  "
        expected = 4
        actual = LengthOfLastWord.lengthOfLastWord(s)
        self.assertEqual(expected, actual)