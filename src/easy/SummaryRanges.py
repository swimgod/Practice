from typing import List


class SummaryRanges:
    @staticmethod
    def summaryRanges(nums: List[int]) -> List[str]:
        ranges = []
        count = 0
        for i in range(len(nums)):
            if i < (len(nums)-1) and (nums[i] + 1) == nums[i+1]:
                count += 1
                continue
            else:
                start_range = nums[i] - count
                end_range = nums[i]
                if start_range == end_range:
                    ranges.append(str(start_range))
                else:
                    ranges.append(f"{start_range}->{end_range}")
                count = 0
        return ranges
