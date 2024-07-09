from typing import List, Optional


class HIndex:
    @staticmethod
    def hIndex(citations: List[int]) -> int:
        sorted_citations = sorted(citations)
        print(sorted_citations)
        return 0