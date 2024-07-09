from unittest import TestCase

from src.medium.HIndex import HIndex


class TestRotateArray(TestCase):
    def test_case1(self):
        citations = [3, 0, 6, 1, 5]
        expected = 3
        actual = HIndex.hIndex(citations)
        self.assertEqual(expected, actual)
