from unittest import TestCase

from src.easy.LongestCommonPrefix import LongestCommonPrefix


class TestLongestCommonPrefix(TestCase):
    def test_case_1(self):
        expected = "fl"
        actual = LongestCommonPrefix.longestCommonPrefix(["flower", "flow", "flight"])
        self.assertEqual(expected, actual)

    def test_case_2(self):
        expected = ""
        actual = LongestCommonPrefix.longestCommonPrefix(["dog","racecar","car"])
        self.assertEqual(expected, actual)

    def test_case_3(self):
        expected = ""
        actual = LongestCommonPrefix.longestCommonPrefix([""])
        self.assertEqual(expected, actual)

    def test_case_4(self):
        expected = "a"
        actual = LongestCommonPrefix.longestCommonPrefix(["a"])
        self.assertEqual(expected, actual)

    def test_case_5(self):
        expected = ""
        actual = LongestCommonPrefix.longestCommonPrefix(["reflower","flow","flight"])
        self.assertEqual(expected, actual)

    def test_case_6(self):
        expected = "a"
        actual = LongestCommonPrefix.longestCommonPrefix(["ac","ac","a","a"])
        self.assertEqual(expected, actual)