class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        res_len = 0

        def expand(l, r):
            nonlocal res, res_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = l
                    res_len = r - l + 1
                l, r = l - 1, r + 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        
        return s[res : res + res_len]

        
            