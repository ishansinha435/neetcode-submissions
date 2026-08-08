class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res, p = [], 0
        while p < len(word1) and p < len(word2):
            res.append(word1[p])
            res.append(word2[p])
            p += 1
        remainder = ""
        if p < len(word1):
            remainder += word1[p::]
        else:
            remainder += word2[p::]
        return ''.join(res) + (remainder)