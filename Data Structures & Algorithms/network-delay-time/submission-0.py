from operator import itemgetter


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = []
        processed = [False] * n
        distance = [float("inf")] * n
        distance[k - 1] = 0
        heapq.heappush(q, (0, k - 1))
        while q:
            top = heapq.heappop(q)[-1]
            if processed[top]:
                continue

            processed[top] = True

            for source, target, time in times:
                if source - 1 == top and distance[source - 1] + time < distance[target - 1]:
                    distance[target - 1] = distance[source - 1] + time
                    heapq.heappush(q, (distance[target - 1], target - 1))
        
        if not all(processed):
            return -1
        return max(distance)
        