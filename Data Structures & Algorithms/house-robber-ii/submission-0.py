class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def robber(start, end):
            memo = {}

            def choose(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(
                    nums[i] + choose(i + 2),  # rob
                    choose(i + 1)             # skip
                )

                return memo[i]

            return choose(start)

        return max(
            robber(0, len(nums) - 2),
            robber(1, len(nums) - 1)
        )