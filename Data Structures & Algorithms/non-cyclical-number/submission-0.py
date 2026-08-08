class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n in seen:
                return False
            if n == 1:
                return True
            seen.add(n)
            new_n = 0
            while n:
                new_n += (n % 10) ** 2
                n //= 10
            n = new_n
        