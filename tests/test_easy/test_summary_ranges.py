from unittest import TestCase

from src.easy.SummaryRanges import SummaryRanges


class TestSummaryRanges(TestCase):
    def test_case_1(self):
        nums = [0, 1, 2, 4, 5, 7]
        expected = ["0->2", "4->5", "7"]
        actual = SummaryRanges.summaryRanges(nums)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]
        expected = ["0", "2->4", "6", "8->9"]
        actual = SummaryRanges.summaryRanges(nums)
        self.assertEqual(expected, actual)
