class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 if (1 << i & n) else 0 for i in range(32))