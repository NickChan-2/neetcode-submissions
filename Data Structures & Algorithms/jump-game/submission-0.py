class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return True
            
            if nums[i] == 0:
                return False

            if i in memo:
                return memo[i]

            end = False
            for j in range(1, nums[i] + 1):
                if dfs(i + j):
                    end = True
                    return True

            memo[i] = end
            return end
        
        return dfs(0)
                    
