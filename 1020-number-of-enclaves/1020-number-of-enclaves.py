class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            grid[r][c] = 0
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= r + dr < n and 0 <= c + dc < m and grid[r + dr][c + dc] == 1:
                    dfs(r + dr, c + dc)
            
        n, m = len(grid), len(grid[0])
        
        for i in range(n):
            for j in [0, m - 1]:
                if grid[i][j] == 1:
                    dfs(i, j)
                    
        for i in [0, n - 1]:
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j)
                    
        return sum([sum(l) for l in grid])