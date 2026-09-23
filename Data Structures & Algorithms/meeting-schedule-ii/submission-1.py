"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        q = []
        res, count = 0, 0
        for i in intervals:
            s, e = i.start, i.end
            while q and q[0] <= s:
                heapq.heappop(q)
                count -= 1
            heapq.heappush(q, e)
            count += 1
            res = max(res, count)
        return res
