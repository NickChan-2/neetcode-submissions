class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # bucketing solution
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        bucket = [[] for _ in range(len(nums) + 1)]

        for v, c in freq.items():
            bucket[c].append(v)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i]:
                for n in bucket[i]:
                    res.append(n)
            
            if len(res) == k:
                return res



        
            
            