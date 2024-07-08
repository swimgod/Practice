from unittest import TestCase

from src.easy.MergeSorted import MergeSorted


class TestMergeSorted(TestCase):
    def test_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        expected = [1, 2, 2, 3, 5, 6]
        MergeSorted.merge(nums1, 3, nums2, 3)
        self.assertEqual(expected, nums1)

    def test_case_2(self):
        nums1 = [1]
        nums2 = []
        expected = [1]
        MergeSorted.merge(nums1, 1, nums2, 0)
        self.assertEqual(expected, nums1)

    def test_case_3(self):
        nums1 = [0]
        nums2 = [1]
        expected = [1]
        MergeSorted.merge(nums1, 0, nums2, 1)
        self.assertEqual(expected, nums1)

    def test_case_4(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        expected = [1, 2, 3, 4, 5, 6]
        MergeSorted.merge(nums1, 3, nums2, 3)
        self.assertEqual(expected, nums1)

    def test_case_5(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        expected = [1, 2, 3, 4, 5, 6]
        MergeSorted.merge_sort(nums1, 3, nums2, 3)
        self.assertEqual(expected, nums1)