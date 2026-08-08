class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1map, s2map = [0] * 26, [0] * 26
        for i, c in enumerate(s1):
            s1map[ord(c) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if s1map == s2map:
                return True
            s2map[ord(s2[r]) - ord('a')] += 1
            s2map[ord(s2[l]) - ord('a')] -= 1
            l += 1
        return s1map == s2map