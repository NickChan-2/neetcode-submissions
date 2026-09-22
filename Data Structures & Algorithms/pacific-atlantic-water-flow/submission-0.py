class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visited, prev):
            # out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # already visited
            if (r, c) in visited:
                return

            # can't travel uphill backwards from ocean
            if heights[r][c] < prev:
                return

            visited.add((r, c))

            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        # top = Pacific
        # bottom = Atlantic
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        # left = Pacific
        # right = Atlantic
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res