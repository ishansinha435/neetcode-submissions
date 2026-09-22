class Solution:
    def getSum(self, a: int, b: int) -> int:
        res, carry = 0, 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            sum_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
            res |= (sum_bit << i)
        
        mask = 0xFFFFFFFF
        if (res >> 31) & 1:
            res = ~(res ^ mask)
     
        return res
                
            