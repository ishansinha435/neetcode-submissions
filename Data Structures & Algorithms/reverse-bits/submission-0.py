class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            last = n & 1
            n >>= 1
            res <<= 1
            res += last
        return res