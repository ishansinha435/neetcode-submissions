class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = {}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i == len(s):
        #         return True
        #     for word in wordDict:
        #         if s.startswith(word, i):
        #             if dfs(i + len(word)):
        #                 dp[i] = True
        #                 return True
        #     dp[i] = False
        #     return False

        # return dfs(0)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s.startswith(word, i) and dp[i + len(word)]:
                    dp[i] = True
                    break
        return dp[0]
        