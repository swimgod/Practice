from typing import List, Optional


class RotateArray:
    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        k = k % len(nums)
        original_values = nums[:len(nums) - k]
        rotated_values = nums[len(nums) - k:]
        nums[:k] = rotated_values
        nums[k:] = original_values

        return None
