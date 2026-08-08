class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hmap = {n : [0, 0] for n in range(1, n + 1)}
        for truster, trusted in trust:
            hmap[truster][1] += 1
            hmap[trusted][0] += 1
        res = -1
        for label, [trusted_by, trusts] in hmap.items():
            if trusted_by == n - 1 and trusts == 0:
                if res != -1:
                    return -1
                res = label
        return res