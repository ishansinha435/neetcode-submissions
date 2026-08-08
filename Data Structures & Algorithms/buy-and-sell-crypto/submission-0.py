class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                maxi = max(maxi, prices[j]-prices[i])
        return maxi