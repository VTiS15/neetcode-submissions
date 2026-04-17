class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [False] * n
        diag1 = [False] * (n + n - 1)
        diag2 = [False] * (n + n - 1)

        def backtrack(y: int = 0, board: List[str] = []):
            if y == n:
                res.append(board.copy())
            else:
                for x in range(n):
                    if col[x] or diag1[x + y] or diag2[x - y + n - 1]:
                        continue

                    board.append("." * x + "Q" + "." * (n - x - 1))
                    col[x] = diag1[x + y] = diag2[x - y + n - 1] = True

                    backtrack(y + 1, board)

                    board.pop()
                    col[x] = diag1[x + y] = diag2[x - y + n - 1] = False
        
        backtrack()
        return res
            