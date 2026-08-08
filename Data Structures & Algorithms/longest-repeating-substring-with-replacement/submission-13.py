class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mfreq = 0
        res = 0
        hmap = {}
        l = 0
        for r, c in enumerate(s):
            hmap[c] = 1 + hmap.get(c, 0)
            mfreq = max(mfreq, hmap[c])
            while r - l + 1 - mfreq > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res