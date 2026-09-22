class Solution:
    def numDecodings(self, s: str) -> int:
        
        # number of ways to decode here you are gonna have to do something along the lines of reading each letter and mapping it. we know the shape of every letter so if something starts with a 0 we can skip it

        # can we do something similair to the palindrome where we use a l r pointer

        # or is this a more classical dp where we memo all the letters we found at x far in the string 
        # then if something is in valid we can just skip or not denote the num

    # what is the base case? 1 letter? so we resolve eventually to one letter through recursion keeping track??

    
        dp = { len(s) : 1 }

        def dfs(i):

            if i in dp: 
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123346")):
                res += dfs(i + 2)
            dp[i] = res

            return res

        return dfs(0)




