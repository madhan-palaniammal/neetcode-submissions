class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m):
                return

            if grid[i][j] != '1':
                return

            grid[i][j] = '2'
            steps = [
                (0, -1), # left
                (0, 1),  # right
                (-1, 0), # up
                (1, 0)   # down
            ]

            for dx, dy in steps:
                dfs(i+dx, j+dy)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1

        return res
