class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        res = 0

        while i < j:
            res = max(res, (j - i) * min(heights[i], heights[j]))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return res
            