class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res, l, r = float('inf'), 1, max(piles)
        while l <= r:
            k = l + (r - l) // 2
            hours = sum((p + k - 1) // k for p in piles)
            if hours <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res