class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        curr_int = intervals[0]
        for i in range(1, len(intervals)):
            if curr_int[1] < intervals[i][0]:
                res.append(curr_int)
                curr_int = intervals[i]
            else:
                curr_int = [curr_int[0], max(curr_int[1], intervals[i][1])]
        res.append(curr_int)
        return res