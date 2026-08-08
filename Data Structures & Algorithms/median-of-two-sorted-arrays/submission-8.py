class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        length = len(A) + len(B)
        sub, sign = divmod(length, 2)
        l, r = 0, len(A) - 1
        while True:
            mA = l + (r - l) // 2
            mB = sub - mA - 2
            Aleft = A[mA] if mA >= 0 else float('-inf')
            Aright = A[mA + 1] if mA + 1 < len(A) else float('inf')
            Bleft = B[mB] if mB >= 0 else float('-inf')
            Bright = B[mB + 1] if mB + 1 < len(B) else float('inf')
            if Aleft <= Bright and Bleft <= Aright:
                if sign:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft < Bright:
                l = mA + 1
            else:
                r = mA - 1