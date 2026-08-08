class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(n):
            count = 0
            while n:
                n = n & (n - 1)
                count += 1
            return count
        return [count_ones(i) for i in range(n + 1)]
