class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = defaultdict(int)
        most = 0
        res = 0
        l = 0 
        for r, c in enumerate(s):
            hmap[c] += 1
            most = max(most, hmap[c])
            while r - l + 1 - most > k:
                hmap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
