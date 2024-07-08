
from typing import List
from itertools import groupby

class IsomorphicStrings:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        char_dict = {}
        char_set = set()

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in char_dict:
                if t_char in char_set:
                    return False
                char_dict[s_char] = t_char
                char_set.add(t_char)
            else:
                if t_char != char_dict[s_char]:
                    return False
        return True


