class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            hmap[course].append(pre) 
        visited, completed = set(), set()
        lst = []

        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True
            visited.add(course)
            for pre in hmap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            lst.append(course)
            completed.add(course)
            return True

        for course in hmap:
            if not dfs(course):
                return []
        return lst