class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            sort = ''.join(sorted(string))
            hashmap[sort].append(string)
        return hashmap.values()
        