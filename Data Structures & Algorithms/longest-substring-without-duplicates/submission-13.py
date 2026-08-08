class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap, longest, l = {}, 0, 0
        for r, c in enumerate(s):
            if c in hmap:
                longest = max(longest, r - l)
                l = max(l, hmap[c] + 1)
            hmap[c] = r
        return max(longest, len(s) - l)
