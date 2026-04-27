class UnionFind:
    def __init__(self, n: int):
        self.link = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while x != self.link[x]:
            x = self.link[x]
        return x
    
    def unite(self, a: int, b: int):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        y_dim, x_dim = len(grid), len(grid[0])
        uf = UnionFind(x_dim * y_dim)
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        res = 0

        for i in range(y_dim):
            for j in range(x_dim):
                if grid[i][j]:
                    for dy, dx in directions:
                        new_i, new_j = i + dy, j + dx

                        if new_i < 0 or new_i >= y_dim or new_j < 0 or new_j >= x_dim or not grid[new_i][new_j]:
                            continue

                        uf.unite(i * x_dim + j, new_i * x_dim + new_j)

                    res = max(res, uf.size[uf.find(i * x_dim + j)])

        return res
        