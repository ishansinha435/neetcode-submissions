class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ""
        for s in strs:
            new += str(len(s)) + "#" + s
        return new

    def decode(self, s: str) -> List[str]:
        res = list()
        while len(s) != 0:
            i = 0
            while s[i] != "#":
                i += 1
            amt = int(s[0:i])
            res.append(s[i+1:i+1+amt])
            s = s[i+1+amt:]
        return res
