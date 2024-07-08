from typing import List


class ValidParentheses:
    @staticmethod
    def isValid(s: str) -> bool:
        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        if (len(s) % 2) != 0:
            return False
        for i in s:
            if i in pairs:
                stack.append(i)
            elif len(stack) == 0 or i != pairs[stack.pop()]:
                return False

        return len(stack) == 0
