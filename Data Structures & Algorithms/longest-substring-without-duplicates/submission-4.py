class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        for i in range(len(s)):
            hashset = set()
            for j in range(i, len(s)):
                if s[j] in hashset:
                    res = max(res, j - i)
                    break
                hashset.add(s[j])
                if j == len(s) - 1:
                    res = max(len(s) - i, res)
        return res

            