class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            sort = ''.join(sorted(s))
            hashmap[sort].append(s)

        res = []
        for l in hashmap:
            res.append(hashmap[l])
        return res

