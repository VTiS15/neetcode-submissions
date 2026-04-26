from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dp(l: int, r: int) -> int:
            if l > r:
                return 0
            return max(nums[l - 1] * nums[i] * nums[r + 1] + dp(l, i - 1) + dp(i + 1, r) for i in range(l, r + 1))
        
        return dp(1, len(nums) - 2)
            