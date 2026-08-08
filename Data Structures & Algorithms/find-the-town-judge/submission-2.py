class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hmap = defaultdict(lambda: [0, 0])
        for truster, trusted in trust:
            hmap[truster][1] += 1
            hmap[trusted][0] += 1
        for label, [trusted_by, trusts] in hmap.items():
            if trusted_by == n - 1 and trusts == 0:
                return label
        return -1