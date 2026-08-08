class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res, l, r = [], 0, 0
        while r < len(s):
            while s[r] != "#":
                r += 1
            l, r = r + 1, r + 1 + int(s[l:r])
            res.append(s[l:r])
            l = r
        return res