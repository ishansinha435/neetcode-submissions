class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        fl, fr = -1, -1
        
        def expand(l, r):
            nonlocal res_len, fl, fr
            length = 0
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l, r = l - 1, r + 1
            l += 1
            r -= 1
            length = r - l + 1
            if length > res_len:
                res_len = length
                fl, fr = l, r

        for i in range(len(s)):
            if i < len(s) + 1:
                expand(i, i + 1)
            expand(i, i)

        return s[fl:fr+1]