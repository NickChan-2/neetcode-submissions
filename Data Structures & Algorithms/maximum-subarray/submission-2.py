class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # have to get this
        # okay lets break the problem down a bit
        # this feels like an obvious memoization we can know the best possible subarray from a position
        # that can just be added
        # logically we go through each. 
        # for each we either choose it or restart from there.
        memo = {}
        def dfs(i):
            if i == len(nums) - 1:
                return nums[i]

            if i in memo:
                return memo[i]

            memo[i] = max(
                nums[i],
                nums[i] + dfs(i + 1)
            )

            return memo[i]

        best = nums[0]

        best = nums[0]
        for i in range(len(nums)):
            best = max(best, dfs(i))

        return best