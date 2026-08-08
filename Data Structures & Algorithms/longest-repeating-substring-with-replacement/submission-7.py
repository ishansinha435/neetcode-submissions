class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = maxF = 0
        hmap = {}
        for r, c in enumerate(s):
            hmap[c] = 1 + hmap.get(c, 0)
            maxF = max(maxF, hmap[c])
            while r - l + 1 - maxF > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            