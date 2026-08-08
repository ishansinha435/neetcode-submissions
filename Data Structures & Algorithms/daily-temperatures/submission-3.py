class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, res = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                old_i = stack.pop()[0]
                res[old_i] = i - old_i
            stack.append((i, t))
        return res