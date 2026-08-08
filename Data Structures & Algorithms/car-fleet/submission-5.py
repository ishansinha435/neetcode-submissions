class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack, data = [], list(zip(position, speed))
        data.sort(reverse = True)
        for p, s in data:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)