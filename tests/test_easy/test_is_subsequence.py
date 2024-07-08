from unittest import TestCase

from src.easy.IsSubsequence import IsSubsequence


class TestIsSubsequence(TestCase):
    def test_case_1(self):
        s = "abc"
        t = "ahbgdc"
        expected = True
        actual = IsSubsequence.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        s = "axc"
        t = "ahbgdc"
        expected = False
        actual = IsSubsequence.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        s = "ab"
        t = "baab"
        expected = True
        actual = IsSubsequence.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        s = "acb"
        t = "ahbgdc"
        expected = False
        actual = IsSubsequence.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        s = "ab"
        t = "badddb"
        expected = True
        actual = IsSubsequence.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        s = "ab"
        t = "abbadddb"
        expected = True
        actual = IsSubsequence.isSubsequence(s, t)
        self.assertEqual(expected, actual)

    def test_case_7(self):
        s = "aaaaaa"
        t = "bbaaaa"
        expected = False
        actual = IsSubsequence.isSubsequence(s, t)
        self.assertEqual(expected, actual)
