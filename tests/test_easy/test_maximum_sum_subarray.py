from unittest import TestCase

from src.easy.FizzBuzz import FizzBuzz


class TestMaximumSumSubarray(TestCase):

    def get_max_sum_subarray(self, arr):
        max_sum = best = 0
        for i in range(len(arr)):
            max_sum = max(arr[i], max_sum + arr[i])
            print(f"max_sum = {max_sum}")
            best = max(best, max_sum)
            print(f"best = {best}")
        return best

    def get_coins(self, input_set, target_sum):
        temp_sum = 0
        coins = []
        while temp_sum != target_sum:
            max_num = max(input_set)
            print(max_num)
            temp_sum += max_num
            if temp_sum > target_sum:
                input_set.remove(max_num)
                temp_sum -= max_num
            else:
                coins.append(max_num)
        return coins

    def get_two_sum(self, arr, target_sum):
        p1 = 0
        p2 = len(arr) - 1
        while (arr[p1] + arr[p2]) != target_sum:
            if (arr[p1] + arr[p2]) > target_sum:
                p2 -= 1
            else:
                p1 += 1
        return [p1, p2]

    def test_case1(self):
        input_arr = [-1, 2, 4, -3, 5, 2, -5, 2]
        expected = 10
        actual = self.get_max_sum_subarray(input_arr)
        self.assertEqual(expected, actual)

    def test_case2(self):
        input_set = {1, 2, 5, 10, 20, 50, 100, 200}
        n = 520
        expected = [200, 200, 100, 20]
        actual = self.get_coins(input_set, n)
        self.assertEqual(expected, actual)

    def test_case3(self):
        input_arr = [2, 7, 11, 15]
        target_sum = 9
        expected = [0, 1]
        actual = self.get_two_sum(input_arr, target_sum)
        self.assertEqual(expected, actual)
