class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res_l, res_r = -1, -1
        
        def check(l, r):
            nonlocal longest, res_l, res_r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            l, r = l + 1, r - 1
            if r - l + 1 > longest:
                longest = r - l + 1
                res_l, res_r = l, r

        for i in range(len(s)):
            check(i, i)
            check(i, i + 1)
        return s[res_l:res_r+1]