class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, l = 0, 0
        for r, n in enumerate(prices):
            if n < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
        return res