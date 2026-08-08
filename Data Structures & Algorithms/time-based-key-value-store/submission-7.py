class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        klist = self.hmap[key]
        klist.sort()
        l, r = 0, len(klist) - 1
        res = (-1, "")
        while l <= r:
            m = l + (r - l) // 2
            if klist[m][0] <= timestamp:
                if klist[m][0] > res[0]:
                    res = klist[m]
                l = m + 1
            else:
                r = m - 1
        return res[1]
                