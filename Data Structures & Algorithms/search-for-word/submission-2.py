class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r, c, i):
            if i >= len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False

            if visited[r][c]:
                return False

            if board[r][c] != word[i]:
                return False

            visited[r][c] = True
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

        

            