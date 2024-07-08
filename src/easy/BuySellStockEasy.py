from typing import List


class BuySellStockEasy:
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        current_max_profit = 0
        for i in range(len(prices)):
            for j in prices[i + 1:]:
                if (j - prices[i]) > current_max_profit:
                    current_max_profit = j - prices[i]
        return current_max_profit

    @staticmethod
    def maxProfit2(prices: List[int]) -> int:
        current_max_profit = 0
        for i in range(len(prices)):
            profit = max(prices[i:]) - prices[i]
            if profit > current_max_profit:
                current_max_profit = profit
        return current_max_profit

    @staticmethod
    def maxProfit3(prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        print(prices)
        print(prices[1:])
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit

