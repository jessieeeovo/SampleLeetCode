class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            grid[r][c] = 1
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= r + dr < n and 0 <= c + dc < m and grid[r + dr][c + dc] == 0:
                    dfs(r + dr, c + dc)
            
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in [0, m - 1]:
                if grid[i][j] == 0:
                    dfs(i, j)
                    
        for i in [0, n - 1]:
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        
        return res