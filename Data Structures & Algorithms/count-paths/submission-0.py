class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dfs(r, c):

            # outside grid
            if r >= m or c >= n:
                return 0

            # reached trophy
            if r == m - 1 and c == n - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            paths = 0

            paths += dfs(r + 1, c)   # down
            paths += dfs(r, c + 1)   # right

            memo[(r, c)] = paths

            return paths

        return dfs(0, 0)