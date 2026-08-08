from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)
        while (abs(len(self.small) - len(self.large)) > 1 or 
            (self.small and self.large and -self.small[0] > self.large[0])):
            if len(self.large) - len(self.small) > 1:
                heappush(self.small, -heappop(self.large))
            else:
                heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2
        
        