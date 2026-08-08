class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        while True:
            if index == len(strs[0]):
                break
            letter = strs[0][index] 
            flag = True
            for s in strs:
                if index == len(s) or s[index] != letter:
                    flag = False
                    break
            if flag:
                index += 1
            else:
                break
        return strs[0][:index]
                
                