class Solution:
    def arrangeCoins(self, n: int) -> int:       
        res = 0
        l, r = 0, n
        while l <= r:
            m = l + (r - l) // 2
            req_coins = (m * (m + 1)) // 2
            if req_coins <= n:
                l = m + 1
                res = m
            else:
                r = m - 1
        return res