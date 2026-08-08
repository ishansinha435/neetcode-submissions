class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        res = 0
        l = 0
        for r, c in enumerate(s):
            if c in hmap:
                l = max(l, hmap[c] + 1)
            hmap[c] = r
            res = max(res, r - l + 1)
        return res
        
