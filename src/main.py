from typing import List


def pair_with_target_sum(arr: List, target: int):
    total = 0
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2:
        cur_sum = arr[p1] + arr[p2]
        if cur_sum == target:
            print([p1, p2])
            return [p1, p2]
        if cur_sum < target:
            p1 += 1
        else:
            p2 -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    target = 6
    # output [1, 3]
    pair_with_target_sum(arr, target)
    arr = [2, 5, 9, 11]
    target = 11
    # output [0, 2]
    pair_with_target_sum(arr, target)
