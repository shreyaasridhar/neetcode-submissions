class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(1, len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                curProfit = prices[r] - prices[l]
                if profit < curProfit:
                    profit = curProfit
        return profit    
            
        