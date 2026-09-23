class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < min_end:
                res += 1
                min_end = min(min_end, intervals[i][1])
            else:
                min_end = intervals[i][1]
        return res
            