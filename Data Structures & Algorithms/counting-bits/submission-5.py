class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0] * (n + 1)
        dp[1] = 1
        highest = 1
        for i in range(1, n + 1):
            if i == highest * 2:
                highest = i
            dp[i] = 1 + dp[i - highest]
        return dp