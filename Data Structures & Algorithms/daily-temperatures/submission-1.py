class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][1]: stack.append((index, temp))
            else: 
                while stack and temp > stack[-1][1]:
                    stackIndex, stackTemp = stack.pop()
                    output[stackIndex] = index - stackIndex
                stack.append((index, temp))
        return output
            

        