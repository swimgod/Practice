from typing import List


class ValidAnagram:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        char_map = {y: t.count(y) for y in t}
        print(char_map)
        if len(s) != len(t):
            return False
        for i in s:
            if i in char_map and char_map[i] != 0:
                char_map[i] -= 1
            else:
                return False
        return True

    @staticmethod
    def isAnagramAlt(s: str, t: str) -> bool:
        return sorted(s) == sorted(t)