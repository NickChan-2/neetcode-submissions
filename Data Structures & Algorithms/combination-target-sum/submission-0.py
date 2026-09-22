class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def findCombo(start, remaining, vals):

            if remaining == 0:
                res.append(vals.copy())
                return

            for i in range(start, len(nums)):

                if nums[i] > remaining:
                    break

                vals.append(nums[i])

                findCombo(i, remaining - nums[i], vals)

                vals.pop()

        findCombo(0, target, [])

        return res