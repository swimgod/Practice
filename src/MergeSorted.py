from typing import List


class MergeSorted:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:m+n] = nums2[:n]
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if nums1[i] < nums1[j]:
                    greater = nums1[i]
                    smaller = nums1[j]
                    nums1[i] = smaller
                    nums1[j] = greater

    @staticmethod
    def merge_sort(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:m+n] = nums2[:n]
        nums1.sort()
