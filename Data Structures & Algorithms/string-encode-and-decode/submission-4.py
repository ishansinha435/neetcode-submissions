class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        l, r, res = 0, 0, []
        while r < len(s):
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            l, r = r + 1, r + length + 1
            res.append(s[l:r])
            l = r
        return res