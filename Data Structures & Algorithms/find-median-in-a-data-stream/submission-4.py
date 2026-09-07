class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        if len(self.small) > len(self.big) + 1 or self.big and self.small[0] > self.big[0]:
            heapq.heappush(self.big, heapq.heappop_max(self.small))
        if len(self.small) + 1 < len(self.big):
            heapq.heappush_max(self.small, heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return self.small[0]
        elif len(self.big) > len(self.small):
            return self.big[0]
        else:
            return (self.small[0] + self.big[0]) / 2