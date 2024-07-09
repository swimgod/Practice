from unittest import TestCase

from src.medium.JumpGame import JumpGame


class TestJumpGame(TestCase):
    def test_case1(self):
        nums = [2, 3, 1, 1, 4]
        expected = True
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)

    def test_case2(self):
        nums = [3, 2, 1, 0, 4]
        expected = False
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)

    def test_case3(self):
        nums = [2, 0]
        expected = True
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)

    def test_case4(self):
        nums = [2, 5, 0, 0]
        expected = True
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)

    def test_case5(self):
        nums = [0]
        expected = True
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)

    def test_case6(self):
        nums = [3, 0, 8, 2, 0, 0, 1]
        expected = True
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)

    def test_case7(self):
        nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
        expected = True
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)

    def test_case8(self):
        nums = [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5,
                1, 7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0,
                1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]
        expected = True
        actual = JumpGame.canJump(nums)
        self.assertEqual(expected, actual)
