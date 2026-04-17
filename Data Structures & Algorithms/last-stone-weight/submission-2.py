import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        first = second = max(stones)
        buckets = [0] * (first + 1)
        for stone in stones:
            buckets[stone] += 1
        
        while first > 0:
            if buckets[first] % 2 == 0:
                first -= 1
                continue
            
            second = first - 1
            while second > 0 and buckets[second] == 0:
                second -= 1
            if second == 0:
                return first
            
            buckets[first] -= 1
            buckets[second] -= 1
            buckets[first - second] += 1

            first = max(first - second, second)

        return first
        