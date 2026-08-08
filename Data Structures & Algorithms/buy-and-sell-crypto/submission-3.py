class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProf = 0
        while r < len(prices):
            currProf = prices[r] - prices[l]
            maxProf = max(maxProf, currProf)
            if currProf < 0:
                l += 1
            else: 
                r += 1
        return maxProf