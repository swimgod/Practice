from typing import List


class RemoveElement:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        count = 0
        nums.sort()
        indexes = []
        for n in range(len(nums)):
            if nums[n] != val:
                count += 1
            else:
                indexes.append(n)
        if len(indexes) > 0:
            del nums[indexes[0]:indexes[-1]+1]
        return count
