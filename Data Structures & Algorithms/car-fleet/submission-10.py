class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack, data = [], list(zip(position, speed))
        data.sort(reverse=True)
        for p, s in data:
            if not stack or (target - p) / s > stack[-1]:
                stack.append((target - p) / s)
        return len(stack)