class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == "0":
                return

            grid[x][y] = "0"

            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res
        