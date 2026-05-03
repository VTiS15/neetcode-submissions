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

        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for node1, node2 in edges:
            uf.unite(node1, node2)

        for i in range(n):
            uf.link[i] = uf.find(i)
        
        return len(set(uf.link))
        