class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        l, r = 0, 0
        res = []
        while r < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l, r = r + 1, r + 1 + length
            res.append(s[l:r])
            l = r
        return res
