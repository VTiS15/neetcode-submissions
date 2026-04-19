class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [height[0]]
        for i in range(1, n):
            prefix.append(max(height[i], prefix[-1]))

        suffix = collections.deque([height[-1]])
        for i in range(n - 2, -1, -1):
            suffix.appendleft(max(height[i], suffix[0]))
        
        return sum(min(prefix[i], suffix[i]) - height[i] for i in range(n))
        
        