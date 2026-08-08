class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        half_size, sign = divmod(len(A) + len(B), 2)
        lA, rA = 0, len(A) - 1
        while True:
            mA = lA + (rA - lA) // 2
            mB = half_size - mA - 2
            leftA = A[mA] if 0 <= mA < len(A) else float('-inf')
            rightA = A[mA + 1] if 0 <= mA + 1 < len(A) else float('inf')
            leftB = B[mB] if 0 <= mB < len(B) else float('-inf')
            rightB = B[mB + 1] if 0 <= mB + 1 < len(B) else float('inf')
            if leftA <= rightB and leftB <= rightA:
                if sign == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA <= rightB:
                lA = mA + 1
            else:
                rA = mA - 1