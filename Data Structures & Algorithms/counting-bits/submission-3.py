class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.count(i) for i in range(0, n + 1)]
        
    def count(self, n):
        res = 0
        while n:
            n &= (n - 1)
            res += 1
        return res