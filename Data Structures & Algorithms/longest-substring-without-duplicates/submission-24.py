class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length, hmap = 0, 0, {}
        for r, c in enumerate(s):
            if c in hmap:
                l = max(l, hmap[c] + 1)
            hmap[c] = r
            length = max(length, r - l + 1)
        return length