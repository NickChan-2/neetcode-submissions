class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def climb(remaining):
            if remaining < 0:
                return 0

            if remaining == 0:
                return 1

            if remaining in memo:
                return memo[remaining]

            memo[remaining] = ( 
                climb(remaining - 1) + climb(remaining - 2)
            )
            return memo[remaining]
        return climb(n)