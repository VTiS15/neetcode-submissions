import heapq


class UnionFind:
    def __init__(self, n):
        self.size = [1] * n
        self.link = list(range(n))

    def find(self, x: int) -> int:
        while x != self.link[x]:
            x = self.link[x]
        return x

    def same(self, a: int, b: int) -> bool:
	    return self.find(a) == self.find(b)

    def unite(self, a: int, b: int):
        a, b = self.find(a), self.find(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = []
        for i in range(1, n):
            for j in range(i):
                heapq.heappush(distances, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))

        res = 0
        uf = UnionFind(n)
        while distances:
            distance, a, b = heapq.heappop(distances)
            if not uf.same(a, b):
                res += distance
                uf.unite(a, b)
        
        return res
        