from unittest import TestCase

from src.IsomorphicStrings import IsomorphicStrings


class TestIsomorphic(TestCase):
    def test_case1(self):
        s = "egg"
        t = "add"
        expected = True
        actual = IsomorphicStrings.isIsomorphic(s, t)
        self.assertEqual(expected, actual)

    def test_case2(self):
        s = "foo"
        t = "bar"
        expected = False
        actual = IsomorphicStrings.isIsomorphic(s, t)
        self.assertEqual(expected, actual)

    def test_case3(self):
        s = "bbbaaaba"
        t = "aaabbbba"
        expected = False
        actual = IsomorphicStrings.isIsomorphic(s, t)
        self.assertEqual(expected, actual)

    def test_case4(self):
        s = "abab"
        t = "baba"
        expected = True
        actual = IsomorphicStrings.isIsomorphic(s, t)
        self.assertEqual(expected, actual)

    def test_case5(self):
        s = "badc"
        t = "baba"
        expected = False
        actual = IsomorphicStrings.isIsomorphic(s, t)
        self.assertEqual(expected, actual)