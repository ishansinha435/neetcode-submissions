class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [0] * len(temperatures), []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_i = stack.pop()[1]
                res[prev_i] = i - prev_i
            stack.append((temp, i))
        return res