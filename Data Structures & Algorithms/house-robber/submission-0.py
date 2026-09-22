class Solution:
    def rob(self, nums: List[int]) -> int:
        # okay so we can either go two current house and jump 2 or skip this one and check the next.

        # so its say as climbing stairs in a nutshell + 2 or +1 but we keep track a number and want the max. we also need the index to pass in to know if weve gon too far

        memo = {}

        def choose(i):

            if i > len(nums) - 1:
                return 0
            
            if i == len(nums) - 1:
                return nums[i]

            # this is memo but it feels wrong again
            # actually no we just need the max from each so if we know the max we can get from each pos we got it
            if i in memo:
                return memo[i]
            memo[i] = max(
                nums[i] + choose(i + 2),
                choose(i + 1)
            )
            return memo[i]

        return choose(0)



