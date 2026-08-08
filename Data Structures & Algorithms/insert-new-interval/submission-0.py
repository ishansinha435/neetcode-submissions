class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        done = False

        for i in intervals:
            if done or newInterval[0] > i[1]: 
                res.append(i)
                continue
            if newInterval[1] < i[0]:
                res.append(newInterval)
                res.append(i)
                done = True
            else:
                newInterval[0] = min(newInterval[0], i[0])
                newInterval[1] = max(newInterval[1], i[1])
        
        if not done:
            res.append(newInterval)
        return res

        
        