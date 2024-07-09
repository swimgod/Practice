from unittest import TestCase

from src.medium.RotateArray import RotateArray


class TestRotateArray(TestCase):
    def test_case1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        RotateArray.rotate(nums, k)
        self.assertEqual(expected, nums)

    def test_case2(self):
        nums = [1, 2]
        k = 5
        expected = [2, 1]
        RotateArray.rotate(nums, k)
        self.assertEqual(expected, nums)
