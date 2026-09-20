class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        smap, tmap = defaultdict(int), Counter(t)
        matches = 0
        l = 0
        res_len = float('inf')
        res = [-1, -1]
        for r, c in enumerate(s):
            smap[c] += 1
            if smap[c] == tmap[c]:
                matches += 1
            while matches == len(tmap):
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                smap[s[l]] -= 1
                if smap[s[l]] + 1 == tmap[s[l]]:
                    matches -= 1
                l += 1
        return "" if res[0] == -1 else s[res[0]:res[1] + 1]