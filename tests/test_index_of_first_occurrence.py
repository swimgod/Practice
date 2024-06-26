from unittest import TestCase

from src.IndexOfFirstOccurrence import IndexOfFirstOccurrence


class TestIndexOfFirstOccurrence(TestCase):
    def test_case_1(self):
        haystack = "sadbutsad"
        needle = "sad"
        expected = 0
        actual = IndexOfFirstOccurrence.strStr(haystack, needle)
        self.assertEqual(expected, actual)