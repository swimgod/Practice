
from typing import List
from itertools import groupby

class IsomorphicStrings:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        s_group = [(i, len(list(j))) for i, j in groupby(s)]
        t_group = [(i, len(list(j))) for i, j in groupby(t)]
        print(s_group)
        print(t_group)
        if len(s_group) != len(t_group):
            return False

        s_index_count = 0
        t_index_count = 0
        for a, b in zip(s_group, t_group):
            s_group_count = a[1]
            t_group_count = b[1]

            if s_group_count != t_group_count:
                return False

            full_s_group = s[s_index_count:s_index_count + s_group_count]
            full_t_group = t[t_index_count:t_index_count + t_group_count]
            s_index_count += s_group_count
            t_index_count += t_group_count
            print(full_s_group)
            print(full_t_group)
        return True
