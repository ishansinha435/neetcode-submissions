class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, l, hmap = 0, 0, {}
        for r, c in enumerate(s):
            if c in hmap:
                l = max(l, hmap[c] + 1)
            hmap[c] = r
            longest = max(longest, r - l + 1)
        return longest