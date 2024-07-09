from typing import List


class FizzBuzz:
    @staticmethod
    def fizzBuzz(n: int) -> List[str]:
        output_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                output_list.append("FizzBuzz")
            elif i % 3 == 0:
                output_list.append("Fizz")
            elif i % 5 == 0:
                output_list.append("Buzz")
            else:
                output_list.append(str(i))
        return output_list

    @staticmethod
    def fizzBuzz2(n: int) -> List[str]:
        output_list = []

        def is_divisible(j: int, k: int):
            return j % k == 0

        for i in range(1, n + 1):
            divisible_three = is_divisible(i, 3)
            divisible_5 = is_divisible(i, 5)

            if divisible_three and divisible_5:
                output_list.append("FizzBuzz")
            elif divisible_three:
                output_list.append("Fizz")
            elif divisible_5:
                output_list.append("Buzz")
            else:
                output_list.append(str(i))
        return output_list
