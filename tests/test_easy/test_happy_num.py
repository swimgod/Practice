from unittest import TestCase

from src.easy.HappyNum import HappyNum


class TestHappyNum(TestCase):
    def test_case1(self):
        n = 19
        expected = True
        actual = HappyNum.isHappy(n)
        self.assertEqual(expected, actual)

    def test_case2(self):
        n = 2
        expected = False
        actual = HappyNum.isHappy(n)
        self.assertEqual(expected, actual)

    def test_case3(self):
        n = 21
        expected = False
        actual = HappyNum.isHappy(n)
        self.assertEqual(expected, actual)