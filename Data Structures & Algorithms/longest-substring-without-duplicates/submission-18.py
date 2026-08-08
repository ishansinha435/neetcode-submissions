class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest, hmap = 0, 0, {}
        for r, c in enumerate(s):
            if s[r] in hmap:
                l = max(l, hmap[c] + 1)
            hmap[c] = r
            longest = max(longest, r - l + 1)
        return longest