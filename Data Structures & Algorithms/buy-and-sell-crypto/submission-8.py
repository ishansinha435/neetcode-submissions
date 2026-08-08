class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res = 0, 0
        for r, p in enumerate(prices):
            if p < prices[l]:
                l = r
            res = max(res, p - prices[l])
        return res