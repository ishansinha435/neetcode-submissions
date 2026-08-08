class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)
        for s in strs:
            sortS = ''.join(sorted(s))
            hashmap[sortS].append(s)
        for key in hashmap:
            res.append(hashmap[key])
        return res
