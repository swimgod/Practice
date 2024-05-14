from typing import List


class LongestCommonPrefix:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        common_sub_strings = set()
        for i in range(len(strs)):
            count = 0
            other_strings = list(set([k for k in strs if k != strs[i]]))
            if len(other_strings) > 0:
                for j in range(len(strs[i])+1):
                    sub_strings = []
                    for k in other_strings:
                        sub_string = strs[i][0:j]
                        if (sub_string != "") & (sub_string in k[0:j]):
                            count += 1
                            sub_strings.append(sub_string)
                    if count == len(set(strs)) - 1:
                        common_sub_strings.add(list(set(sub_strings))[0])
                    count = 0
                    sub_strings.clear()
            else:
                return strs[i]
        return max(list(common_sub_strings)) if len(list(common_sub_strings)) > 0 else ""
