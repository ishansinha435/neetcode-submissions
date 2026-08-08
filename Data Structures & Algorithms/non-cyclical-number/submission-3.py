class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = self.sumSquares(n), n
        while True:
            if fast == 1 or slow == 1:
                return True
            if fast == slow:
                return False
            fast = self.sumSquares(self.sumSquares(fast))
            slow = self.sumSquares(slow)

    def sumSquares(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res
        