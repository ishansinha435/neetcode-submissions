class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res, l, r = float('inf'), 1, max(piles)
        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res