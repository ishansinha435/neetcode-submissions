class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float('inf')
        min_l, min_r = -1, -1
        l = 0
        tmap, smap = Counter(t), defaultdict(int)
        matches = 0
        need = len(tmap)
        for r, c in enumerate(s):
            smap[c] += 1
            if smap[c] == tmap[c]:
                matches += 1
            while matches == need:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_l, min_r = l, r
                if smap[s[l]] == tmap[s[l]]:
                    matches -= 1
                smap[s[l]] -= 1
                l += 1
        return "" if min_l == -1 and min_r == -1 else s[min_l:min_r+1]
