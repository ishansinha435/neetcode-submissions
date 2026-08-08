class Solution:
    def climbStairs(self, n: int) -> int:
        hmap = {}

        def recurse(n):
            if n == 0:
                return 1
            if n < 0:
                return 0

            if n - 1 in hmap:
                one = hmap[n - 1] 
            else:
                one = recurse(n - 1)
                hmap[n - 1] = one

            if n - 2 in hmap:
                two = hmap[n - 2] 
            else:
                two = recurse(n - 2)
                hmap[n - 2] = two

            return one + two
        
        return recurse(n)