class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(i,j):
            if (i<0 or j<0 or i>=ROWS or j >= COLS or grid[i][j] == "0"):
                return
            grid[i][j] = "0"
            for dr, dc in directions:
                dfs(i + dr, j + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r,c)
                    islands += 1
        return islands