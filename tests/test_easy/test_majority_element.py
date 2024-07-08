from unittest import TestCase

from src.easy.MajorityElement import MajorityElement


class TestMajorityElement(TestCase):
    def test_case_1(self):
        nums = [3, 2, 3]
        expected = 3
        actual = MajorityElement.majorityElement(nums)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        nums = [3, 3, 4]
        expected = 3
        actual = MajorityElement.majorityElement(nums)
        self.assertEqual(expected, actual)
