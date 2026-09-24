class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # my mind is telling me we could do something where we find something 
        # that has a number we check the num and see all the possibilities after
        # if we do something where we memoize and if we keep the max length from that spot.
        # we skip if its less
        # and we stop if the index is higher than the len

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            best = 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            memo[i] = best
            return best

        long = 1
        for i in range(len(nums)):
            long = max(long, dfs(i))
        
        return long
        
            