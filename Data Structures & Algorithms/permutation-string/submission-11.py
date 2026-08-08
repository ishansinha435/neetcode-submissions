class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map1, map2 = {}, {}
        for i in range(len(s1)):
            map1[s1[i]] = 1 + map1.get(s1[i], 0)
            map2[s2[i]] = 1 + map2.get(s2[i], 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if map1 == map2:
                return True
            map2[s2[r]] = 1 + map2.get(s2[r], 0)
            map2[s2[l]] -= 1
            if map2[s2[l]] == 0:
                map2.pop(s2[l])
            l += 1
        return map1 == map2

