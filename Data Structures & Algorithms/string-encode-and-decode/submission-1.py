class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j != len(s):
            while s[j] != "#":
                j += 1
            num = int(s[i:j])
            i = j + 1
            j += num + 1
            res.append(s[i:j])
            i = j
        return res