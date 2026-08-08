class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map1, map2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1
        l = 0
        for r, c in enumerate(s2):
            if map1 == map2:
                return True
            if r < len(s1):
                continue
            map2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            map2[ord(c) - ord('a')] += 1
        return map1 == map2