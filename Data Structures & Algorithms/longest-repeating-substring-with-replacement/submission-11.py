class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res, hmap, max_f = 0, 0, {}, 0
        for r, c in enumerate(s):
            hmap[c] = 1 + hmap.get(c, 0)
            max_f = max(max_f, hmap[c])
            while r - l + 1 - max_f > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
