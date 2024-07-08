from unittest import TestCase

from src.RemoveElement import RemoveElement


class TestRemoveElement(TestCase):
    def test_case_1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected = [2, 2]
        k = RemoveElement.removeElement(nums, val)
        self.assertEqual(sorted(expected), nums[:k])

    def test_case_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected = [0, 1, 4, 0, 3]
        k = RemoveElement.removeElement(nums, val)
        self.assertEqual(sorted(expected), nums[:k])

    def test_case_3(self):
        nums = []
        val = 0
        expected = []
        k = RemoveElement.removeElement(nums, val)
        self.assertEqual(sorted(expected), nums[:k])
