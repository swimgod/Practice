from unittest import TestCase

from src.BuySellStockEasy import BuySellStockEasy


class TestBuySellStockEasy(TestCase):
    def test_case_1a(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        actual = BuySellStockEasy.maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_case_1b(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        actual = BuySellStockEasy.maxProfit3(prices)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        actual = BuySellStockEasy.maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_case_2c(self):
        prices = [7, 6, 4, 3, 1]
        expected = 0
        actual = BuySellStockEasy.maxProfit3(prices)
        self.assertEqual(expected, actual)

    def test_case_2ca(self):
        prices = [7, 4, 1, 3, 1, 4]
        expected = 3
        actual = BuySellStockEasy.maxProfit3(prices)
        self.assertEqual(expected, actual)

    def test_case_3(self):
        prices = [900, 510, 174, 329, 873, 382, 279, 855, 396, 810, 322, 192]
        expected = 699
        actual = BuySellStockEasy.maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_case_4(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        actual = BuySellStockEasy.maxProfit2(prices)
        self.assertEqual(expected, actual)

    def test_case_5(self):
        prices = [7, 2, 5, 2, 6, 4]
        expected = 4
        actual = BuySellStockEasy.maxProfit2(prices)
        self.assertEqual(expected, actual)

    def test_case_6(self):
        prices = [2, 4, 1]
        expected = 2
        actual = BuySellStockEasy.maxProfit2(prices)
        self.assertEqual(expected, actual)

    def test_case_6c(self):
        prices = [2, 4, 1]
        expected = 2
        actual = BuySellStockEasy.maxProfit3(prices)
        self.assertEqual(expected, actual)

    def test_case_7(self):
        prices = [7, 2, 5, 2, 6, 4]
        expected = 4
        actual = BuySellStockEasy.maxProfit3(prices)
        self.assertEqual(expected, actual)

    def test_case_8(self):
        prices = [3, 3, 5, 0, 0, 3, 1, 4]
        expected = 4
        actual = BuySellStockEasy.maxProfit3(prices)
        self.assertEqual(expected, actual)
