class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        placed = False
        for i in range(len(intervals)):
            s, e = intervals[i]
            if placed:
                res.append(intervals[i])
                continue
            if newInterval[1] < s:
                res.append(newInterval)
                res.append(intervals[i])
                placed = True
            elif newInterval[0] > e:
                res.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], s)
                newInterval[1] = max(newInterval[1], e)   
        if not placed:
            res.append(newInterval)
        return res