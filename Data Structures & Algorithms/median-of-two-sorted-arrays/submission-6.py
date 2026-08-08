class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        length, sign = divmod(len(A) + len(B), 2)
        l, r = 0, len(A) - 1

        while True:
            mA = l + (r - l) // 2
            mB = length - mA - 2

            leftA = A[mA] if mA >= 0 else float('-inf')
            rightA = A[mA + 1] if mA + 1 < len(A) else float('inf')
            leftB = B[mB] if mB >= 0 else float('-inf')
            rightB = B[mB + 1] if mB + 1 < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if sign == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA <= rightB:
                l = mA + 1
            else:
                r = mA - 1

