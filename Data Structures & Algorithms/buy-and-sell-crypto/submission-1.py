class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = profit = 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            if prices[R] - prices[L] > profit:
                profit = prices[R] - prices[L]

        return profit