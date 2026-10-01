class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1map = Counter(s1)
        s2map = Counter()
        for i in range(len(s1)):
            s2map[s2[i]] += 1
        if s1map == s2map:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            s2map[s2[r]] += 1
            s2map[s2[l]] -= 1
            if s1map == s2map:
                return True
            l += 1
        return False