class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, res, white = 0, k, 0
        for r, c in enumerate(blocks):
            if blocks[r] == "W":
                white += 1
            if r - l + 1 > k:
                if blocks[l] == "W":
                    white -= 1
                l += 1
            if r - l + 1 == k and white < res:
                res = white
        return res
            