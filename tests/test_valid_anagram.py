from unittest import TestCase

from src.ValidAnagram import ValidAnagram


class TestValidAnagram(TestCase):
    def test_case1(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        actual = ValidAnagram.isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_case2(self):
        s = "rat"
        t = "car"
        expected = False
        actual = ValidAnagram.isAnagram(s, t)
        self.assertEqual(expected, actual)

    def test_case3(self):
        s = "a"
        t = "ab"
        expected = False
        actual = ValidAnagram.isAnagram(s, t)
        self.assertEqual(expected, actual)