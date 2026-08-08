class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, longest = 0, 0
        hp = {}
        for r, c in enumerate(s):
            if c in hp:
                l = max(hp[c] + 1, l)
            hp[c] = r
            longest = max(longest, r - l + 1)
        return longest