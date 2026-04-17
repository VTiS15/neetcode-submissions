from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for ticket in tickets:
            heappush(adj[ticket[0]], ticket[1])

        res = []
        path = ["JFK"]

        while path:
            airport = path[-1]
            if adj[airport]:
                path.append(heappop(adj[airport]))
            else:
                res.append(path.pop())
        
        res.reverse()

        return res
        