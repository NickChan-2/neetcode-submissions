class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      # my assumption here is taht i would do something where i start at both ends right the full thing and work in eliminating sides

      # another perhaps more interesting choice is to do something where i choose either to continue a sub array or not. then we cover all possibilities and we can memoize that i believe

      # teh problem with that memoization is that i cant just save the index because theres multiple way to be at that. but the best at that. the max number maybe. but again it only really works
      
      # ill just do brute first
    # base case is the end of the list of nums
    # we can have the best initially be 0
    # we can do something where we either use this in the current running total or start a new one at that position

    # so 1 * dfs(i) or total *= dfs(i + 1)

    # the recursive case is that we either choose to start a new subarry or continue the existing one

    # not sure you can memo because a neg number isnt always worse than a positive one if another neg comes
        cur_max = nums[0]
        cur_min = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            prev_max = cur_max
            prev_min = cur_min

            cur_max = max(
                x,                  # start new
                x * prev_max,       # continue max
                x * prev_min        # negative might flip
            )

            cur_min = min(
                x,
                x * prev_max,
                x * prev_min
            )

            best = max(best, cur_max)

        return best