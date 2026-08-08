class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.hmap[key]
        l, r = 0, len(timestamps) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if timestamps[m][0] <= timestamp:
                res = timestamps[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
