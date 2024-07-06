from typing import List


class HappyNum:
    @staticmethod
    def isHappy(n: int) -> bool:
        def sum_of_squares(k: str) -> bool:
            total = 0
            for i in range(len(k)):
                total += int(k[i])**2
            if total == 1:
                return True
            else:
                return sum_of_squares(str(total))

        try:
            return sum_of_squares(str(n))
        except RecursionError:
            return False

    @staticmethod
    def isHappy2(n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1
