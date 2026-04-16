import functools


class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def dp(start: int = 0) -> int:
            if start >= len(nums):
                return 0
            return max(nums[start] + dp(start + 2), dp(start + 1))
        
        return dp()
        