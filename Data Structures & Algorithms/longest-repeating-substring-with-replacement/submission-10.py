class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_f, res = 0, 0, 0
        count = {}
        for r, c in enumerate(s):
            count[c] = 1 + count.get(c, 0)
            max_f = max(max_f, count[c])
            while r - l + 1 - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
