class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res = 0, 0
        for r, p in enumerate(prices):
            while l < r and p <= prices[l]:
                l += 1
            res = max(res, p - prices[l])
        return res