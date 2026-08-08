class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        while i >= -1 * len(digits) and digits[i] == 9:
            digits[i] = 0
            i -= 1
        if i < -1 * len(digits):
            return [1] + digits
        else:
            digits[i] += 1
        return digits