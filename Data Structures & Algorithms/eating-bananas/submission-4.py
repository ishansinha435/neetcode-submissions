class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r - l) // 2
            numHours = 0
            for pile in piles:
                numHours += (pile + m - 1) // m
            if numHours <= h:
                r = m
            else:
                l = m + 1
        return r
            