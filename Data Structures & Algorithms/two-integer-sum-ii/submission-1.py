class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            
            if target == (numbers[left] + numbers[right]):
                return [left + 1, right + 1]
            elif target > (numbers[left] + numbers[right]):
                left += 1
            else:
                right -= 1
        