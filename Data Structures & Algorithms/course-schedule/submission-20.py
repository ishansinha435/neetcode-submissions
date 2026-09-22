class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = defaultdict(list)
        for crs, pre in prerequisites:
            hmap[crs].append(pre)
        visited = set()
        memo = {}
        
        def dfs(i):
            if hmap[i] == []:
                return True
            if i in visited:
                return False
            visited.add(i)
            res = True
            for crs in hmap[i]:
                if not dfs(crs):
                    res = False
            visited.remove(i)
            if res:
                hmap[i] = []
            return res
        
        return all(dfs(i) for i in range(numCourses))