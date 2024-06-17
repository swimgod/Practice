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
        min_test = 0
        max_test = 0
        print(prices)

        def clean():
            min_idxs = [i for i, x in enumerate(prices) if x == min(prices)]
            max_idxs = [i for i, x in enumerate(prices) if x == max(prices)]
            min_idx = max(max_idxs)
            max_idx = min(min_idxs)
            print(f"min_idxs: {min_idxs}")
            print(f"max_idxs: {max_idxs}")
            print(f"max_idx: {max_idx}")
            print(f"min_idx: {min_idx}")

            if max_idx < min_idx:
                del prices[max_idx]
                clean()

        clean()
        print(prices)
        return prices[max_test] - prices[min_test]

