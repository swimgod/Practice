from typing import List


class TwoSumSolution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        for i in nums:
            first_index = nums.index(i)
            for j in nums[first_index + 1:]:
                if (i + j) == target:
                    return [first_index, nums.index(j, first_index + 1, len(nums))]
