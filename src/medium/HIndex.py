from typing import List, Optional
import math

class HIndex:
    @staticmethod
    def hIndex(citations: List[int]) -> int:
        citations.sort()
        h = 0
        length = len(citations)
        print(citations)
        for i in range(length):
            print(f"{citations[i]} >= {length - i}")
            if citations[i] >= length - i:
                h += 1

        return h