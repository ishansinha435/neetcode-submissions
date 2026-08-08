class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i in range(len(s)):
            chars = set(s[i])
            length = 1
            for j in range(i + 1, len(s)):
                if s[j] in chars: break
                chars.add(s[j])
                length += 1
            maxLength = max(maxLength, length)
        return maxLength
            
