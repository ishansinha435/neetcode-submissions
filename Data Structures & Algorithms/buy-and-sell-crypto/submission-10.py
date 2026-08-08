class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            res = max(res, profit)
        return res