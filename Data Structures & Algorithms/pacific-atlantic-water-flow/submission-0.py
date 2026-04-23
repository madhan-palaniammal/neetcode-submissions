class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R = len(heights)
        C = len(heights[0])

        pacific = [[0 for _ in range(C)] for _ in range(R)]
        atlantic = [[0 for _ in range(C)] for _ in range(R)]

        def dfs(i, j, ocean):
            ocean[i][j] = 1
            paths = [
                [0, 1],
                [0, -1],
                [1, 0],
                [-1, 0]
            ]

            for dx, dy in paths:
                new_i = i + dx
                new_j = j + dy
                if (
                    0 <= new_i < R
                    and 0 <= new_j < C
                    and heights[i][j] <= heights[new_i][new_j]
                    and ocean[new_i][new_j] == 0
                ):
                    dfs(new_i, new_j, ocean)

        for r in range(R):
            dfs(r, 0, pacific)
            dfs(r, C-1, atlantic)
        for c in range(C):
            dfs(0, c, pacific)
            dfs(R-1, c, atlantic)

        res = []
        for i in range(R):
            for j in range(C):
                if pacific[i][j] + atlantic[i][j] == 2:
                    res.append([i, j])

        return res