from unittest import TestCase

from src.medium.HIndex import HIndex


class TestHIndex(TestCase):
    def test_case1(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        actual = HIndex.hIndex(citations)
        self.assertEqual(expected, actual)

    def test_case2(self):
        citations = [1, 3, 1]
        expected = 1
        actual = HIndex.hIndex(citations)
        self.assertEqual(expected, actual)

    def test_case3(self):
        citations = [0]
        expected = 0
        actual = HIndex.hIndex(citations)
        self.assertEqual(expected, actual)

    def test_case4(self):
        citations = [1, 1]
        expected = 1
        actual = HIndex.hIndex(citations)
        self.assertEqual(expected, actual)