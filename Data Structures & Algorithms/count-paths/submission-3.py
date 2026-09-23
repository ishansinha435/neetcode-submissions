class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rt, rb = [0] * n, [1] * n
        for r in range(m - 2, -1, -1):
            for c in range(n - 1, -1, -1):
                rt[c] = rb[c] + (rt[c + 1] if c + 1 < n else 0)
            rb = rt
        return rb[0]