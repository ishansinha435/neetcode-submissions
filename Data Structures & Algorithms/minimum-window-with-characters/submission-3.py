class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = None
        res_len = float('inf')
        tmap = Counter(t)
        smap = {}
        l = 0
        matches = 0
        for r, c in enumerate(s):
            smap[c] = 1 + smap.get(c, 0)
            if c in tmap and smap[c] == tmap[c]:
                matches += 1
            while matches == len(tmap):
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = (l, r)
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] + 1 == tmap[s[l]]:
                    matches -= 1
                l += 1
        return "" if not res else s[res[0]:res[1]+1]
            