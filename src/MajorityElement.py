from typing import List


class MajorityElement:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        count = {}
        for n in list(set(nums)):
            count[n] = nums.count(n)
        return max(count, key=count.get)
