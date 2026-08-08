class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)] 
        count = dict()
        res = []

        for n in nums:
            count[n] =  1 + count.get(n, 0)
        for n, c in count.items():
            bucket[c].append(n)
        for i in range(len(nums), -1, -1):
            for n in bucket[i]:
                res.append(n)
            if(len(res) == k):
                return res
        return

            
        
        
        