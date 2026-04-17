class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """This problem is equivalent to finding the lexicographically smallest Eulerian path.
        
        Procedure:
            1. Create adjacency heap, treating each ticket as an edge.
            2. Use Hierholzer's algorithm to find the lexicographically smallest flight path.

        """
        adj = collections.defaultdict(list)
        for ticket in tickets:
            heapq.heappush(adj[ticket[0]], ticket[1])

        res = []
        path = ["JFK"]  # Stack

        while path:
            airport = path[-1]
            if adj[airport]:
                path.append(heapq.heappop(adj[airport]))
            else:
                res.append(path.pop())

        res.reverse()
        return res
        