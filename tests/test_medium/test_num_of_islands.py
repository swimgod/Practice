from unittest import TestCase

from src.medium.NumOfIslands import NumOfIslands


class TestHIndex(TestCase):
    def test_case1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1
        actual = NumOfIslands.numIslands(grid)
        self.assertEqual(expected, actual)

    def test_case2(self):
        grid = [
            ["0", "0", "0", "0", "0"],
            ["1", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "1"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 2
        actual = NumOfIslands.numIslands(grid)
        self.assertEqual(expected, actual)
