class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count, time = 0, 0
        for i in range(len(position)):
            position[i] = (position[i], speed[i])
        position.sort()
        while position:
            (p, s) = position.pop()
            currTime = (target - p) / s
            if currTime > time: 
                count += 1
                time = currTime
        return count