class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # okay so this feels like i should keep a remining value that i pass through
        # at each pass i can try and add/subtract to the target to get a val
        # we can keep the min. so something where we decide whats the min and return the min

        # okay base case here is that we get remaining to 0
        # so how can we denote how many coins it took to get there
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0

            if remaining < 0:
                return amount + 1

            if remaining in memo:
                return memo[remaining]

            best = amount + 1

            for coin in coins:
                candidate = 1 + dfs(remaining - coin)
                best = min(best, candidate)

            memo[remaining] = best
            return best


        num = dfs(amount)

        if num > amount:
            return -1
        else:
            return num
