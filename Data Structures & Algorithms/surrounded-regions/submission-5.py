class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i: int, j: int, visited = None):
            if not visited:
                visited = []

            if (i, j) in visited:
                return visited
            if i in (0, m - 1) or j in (0, n - 1):
                return []

            visited.append((i, j))

            for dy, dx in directions:
                ni, nj = i + dy, j + dx
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == "O" and len(dfs(ni, nj, visited)) < len(visited):
                    return []

            return visited
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O":
                    for y, x in dfs(i, j):
                        board[y][x] = "X"
        