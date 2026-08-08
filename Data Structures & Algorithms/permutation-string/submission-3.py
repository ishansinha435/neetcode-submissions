class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1, map2 = {}, {}
        if len(s2) < len(s1): return False
        for i in range(len(s1)):
            map1[s1[i]] = 1 + map1.get(s1[i], 0)
            map2[s2[i]] = 1 + map2.get(s2[i], 0)
        
        l, r = 0, len(s1) - 1
        while r < len(s2) - 1:
            if map1 == map2:
                return True
            map2[s2[l]] -= 1
            if map2[s2[l]] == 0:
                map2.pop(s2[l])
            l, r = l + 1, r + 1
            map2[s2[r]] = 1 + map2.get(s2[r], 0)
        return map1 == map2
            
