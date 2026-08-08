class Solution:
    def minOperations(self, s: str) -> int:
        count1, count2 = 0, 0
        for i, c in enumerate(s):
            if i % 2 == 0 and c == "0":
                count1 += 1
            elif i % 2 == 1 and c == "1":
                count1 += 1
        for i, c in enumerate(s):
            if i % 2 == 0 and c == "1":
                count2 += 1
            elif i % 2 == 1 and c == "0":
                count2 += 1
        return min(count1, count2)