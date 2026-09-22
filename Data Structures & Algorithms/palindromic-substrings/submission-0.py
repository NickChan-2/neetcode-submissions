class Solution:
    def countSubstrings(self, s: str) -> int:
        num = 0

        def find(l, r):
            nonlocal num

            while l >= 0 and r < len(s) and s[l] == s[r]:
                num += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            find(i, i)       # odd-length palindromes
            find(i, i + 1)   # even-length palindromes

        return num