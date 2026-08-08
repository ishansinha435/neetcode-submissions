class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap, tmap = {}, {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        l, need, res = 0, 0, (-1, float('inf'))
        for r, c in enumerate(s):
            smap[c] = 1 + smap.get(c, 0)
            if c in tmap and smap[c] == tmap[c]:
                need += 1
            while need == len(tmap):
                if r - l < res[1] - res[0]:
                    res = (l, r)
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    need -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res[0] != -1 else ""