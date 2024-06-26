from typing import List


class LengthOfLastWord:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        return len([a for a in s.split(" ") if a != ""][-1])