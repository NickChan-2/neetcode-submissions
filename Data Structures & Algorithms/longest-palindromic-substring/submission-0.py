class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        def expand(l, r):
            nonlocal longest

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(longest):
                    longest = s[l:r + 1]

                l -= 1
                r += 1

        for i in range(len(s)):
            # odd length palindrome
            expand(i, i)

            # even length palindrome
            expand(i, i + 1)

        return longest