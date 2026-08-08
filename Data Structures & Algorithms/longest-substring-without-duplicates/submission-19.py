class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res, hmap = 0, 0, {}
        for r, c in enumerate(s):
            if c in hmap:
                l = max(l, hmap[c] + 1)
            res = max(res, r - l + 1)
            hmap[c] = r
        return res