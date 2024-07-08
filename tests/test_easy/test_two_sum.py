from unittest import TestCase

from src.easy.TwoSumSolution import TwoSumSolution


class TestTwoSum(TestCase):

    def test_case_1(self):
        expected = [0, 1]
        actual = TwoSumSolution.two_sum([2, 7, 11, 15], 9)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        expected = [1, 2]
        actual = TwoSumSolution.two_sum([3, 2, 4], 6)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        expected = [0, 1]
        actual = TwoSumSolution.two_sum([3, 3], 6)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        expected = [0, 2]
        actual = TwoSumSolution.two_sum([3, 2, 3], 6)
        self.assertEqual(expected, actual)
