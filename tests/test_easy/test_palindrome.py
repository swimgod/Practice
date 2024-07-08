from unittest import TestCase

from src.easy.PalindromeSolution import PalindromeSolution


class TestPalindrome(TestCase):
    def test_case_1(self):
        expected = True
        actual = PalindromeSolution.is_palindrome(121)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        expected = False
        actual = PalindromeSolution.is_palindrome(-121)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        expected = True
        actual = PalindromeSolution.is_palindrome(1221)
        self.assertEqual(expected, actual)
