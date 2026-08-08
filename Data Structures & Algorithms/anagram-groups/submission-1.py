class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for string in strs:
            sort = ''.join(sorted(string))
            if sort in hashmap:
                hashmap[sort].append(string)
            else:
                hashmap[sort] = [string]
        return hashmap.values()
        