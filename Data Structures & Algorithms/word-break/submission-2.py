class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # okay my thought is we do something where we find a first letter and slice

        # so essentially make a dictionary of words starting with the letter.
        # and save lengths of each word and we can slice there multiple times
        # then we can just walk forward through it

        pages = {}

        # get a dictionary pages per starting letter
        for word in wordDict:
            if word[0] in pages:
                pages[word[0]].append(len(word))
            else:
                pages[word[0]] = [len(word)]

        memo = {}
        def dfs(i):
            # succesful split
            if i == len(s):
                return True

            if i > len(s):
                return False

             # unsuccesful split
            if s[i] not in pages:
                return False

            if i in memo:
                return memo[i]

            for n in pages[s[i]]:
                sub = s[i:i+n]
                if sub not in wordDict:
                    continue
                if dfs(i + n):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)
            




