class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hmap, res = {}, 0
        while r < len(s):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            curr_wind, most_freq = r - l + 1, max(hmap.values())
            if curr_wind - most_freq > k:
                hmap[s[l]] -= 1
                hmap[s[r]] -= 1
                l += 1
            else:
                res = max(res, curr_wind)
                r += 1
        return res