class Solution:
    def minWindow(self, s: str, t: str) -> str:
        smap, tmap = {}, {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        l, shortest = 0, (0, float('inf'))
        have, need = 0, len(tmap)
        for r, c in enumerate(s):
            smap[c] = 1 + smap.get(c, 0)
            if c in tmap and smap[c] == tmap[c]:
                have += 1
            if have == need:
                while True:
                    if r - l < shortest[1] - shortest[0]:
                        shortest = (l, r)
                    smap[s[l]] -= 1
                    if s[l] in tmap and tmap[s[l]] == smap[s[l]] + 1:
                        have -= 1
                        l += 1
                        break
                    l += 1
        left, right = shortest
        return "" if right == float('inf') else s[left : right + 1]


