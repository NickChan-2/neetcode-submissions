class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def search(r, c):

            # outside grid
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            # water / already visited
            if grid[r][c] == '0':
                return

            # mark visited
            grid[r][c] = '0'

            search(r - 1, c)
            search(r + 1, c)
            search(r, c - 1)
            search(r, c + 1)

        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == '1':
                    islands += 1
                    search(r, c)

        return islands