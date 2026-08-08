class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap, longest, l = {}, 0, 0
        for r, c in enumerate(s):
            if c in hmap:
                l = max(l, hmap[c] + 1)
            longest = max(longest, r - l + 1)
            hmap[c] = r
        return longest