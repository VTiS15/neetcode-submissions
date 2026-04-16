import functools


class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def dp(start: int = 0, end: int = len(nums) - 1) -> int:
            if start > end:
                return 0
            return max(nums[start] + dp(start + 2, end), dp(start + 1, end))
        
        return dp()
        