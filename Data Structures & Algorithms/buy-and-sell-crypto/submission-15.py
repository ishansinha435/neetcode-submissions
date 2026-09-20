class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0
        for r, p in enumerate(prices):
            if p < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res
