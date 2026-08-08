class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        if self.large and self.small[0] > self.large[0]:
            big = heapq.heappop_max(self.small)
            heapq.heappush(self.large, big)
        while abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                big = heapq.heappop_max(self.small)
                heapq.heappush(self.large, big)
            else:
                little = heapq.heappop(self.large)
                heapq.heappush_max(self.small, little)

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return self.small[0]
        else:
            return (self.large[0] + self.small[0]) / 2
        