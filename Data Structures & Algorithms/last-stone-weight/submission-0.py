import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq.heapify_max(stones)
            heapq.heappush_max(stones, heapq.heappop_max(stones) - heapq.heappop_max(stones))
        
        return stones[0]
        