class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c):
            m, n = len(grid), len(grid[0])
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            # delta-directions
            dd = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dd:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    dfs(grid, r + dr, c + dc)
            
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                # for every new island found
                if grid[i][j] == "1":
                    res += 1
                    # use dfs to convert all connected grids to 0
                    dfs(grid, i, j)
        return res