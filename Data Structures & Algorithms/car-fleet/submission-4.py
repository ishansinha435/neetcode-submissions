class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack, data = [], []
        for i in range(len(position)):
            data.append((position[i], speed[i]))
        data.sort()
        for i in range(len(data) - 1, -1, -1):
            time = (target - data[i][0]) / data[i][1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)