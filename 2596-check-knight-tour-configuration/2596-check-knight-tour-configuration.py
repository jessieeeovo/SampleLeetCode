class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # Weekly Contest 337, 03/19/2023
        if grid[0][0] != 0:
            return False
        r = 0
        c = 0
        n = len(grid)
        dd = [[1, 2], [2, 1], [-1, 2], [-2, 1],[1, -2], [2, -1], [-1, -2], [-2, -1]]
        for t in range(1, n * n):
            found = False
            for dr, dc in dd:
                if 0 <= r + dr < n and 0 <= c + dc < n and grid[r + dr][c + dc] == t:
                    found = True
                    break
            if not found:
                return False
            r += dr
            c += dc
            found = False
        return True
            
                    