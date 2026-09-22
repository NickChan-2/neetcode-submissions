class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        longest = 0
        window = set()

        while right < len(s):

            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])
            right += 1

            longest = max(longest, len(window))
        
        return longest