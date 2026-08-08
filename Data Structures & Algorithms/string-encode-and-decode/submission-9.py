class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        res, l, r = [], 0, 0
        while r < len(s):
            while s[r] != "#":
                r += 1
            l, r = r + 1, r + 1 + int(s[l:r])
            res.append(s[l:r])
            l = r
        return res
