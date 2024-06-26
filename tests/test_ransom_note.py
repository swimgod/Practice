from unittest import TestCase

from src.RansomNote import RansomNote


class TestRansomNote(TestCase):
    def test_case1(self):
        ransom_note = "a"
        magazine = "b"
        expected = False
        actual = RansomNote.canConstruct(ransom_note, magazine)
        self.assertEqual(expected, actual)

    def test_case2(self):
        ransom_note = "aa"
        magazine = "ab"
        expected = False
        actual = RansomNote.canConstruct(ransom_note, magazine)
        self.assertEqual(expected, actual)

    def test_case3(self):
        ransom_note = "aa"
        magazine = "aab"
        expected = True
        actual = RansomNote.canConstruct(ransom_note, magazine)
        self.assertEqual(expected, actual)