class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for ticket in tickets:
            heapq.heappush(adj[ticket[0]], ticket[1])

        res = []
        path = ["JFK"]

        while path:
            airport = path[-1]
            if adj[airport]:
                path.append(heapq.heappop(adj[airport]))
            else:
                res.append(path.pop())

        return res[::-1]
        