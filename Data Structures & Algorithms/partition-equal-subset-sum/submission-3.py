from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        n = len(nums)
        target = s // 2
        
        @cache
        def dp(i: int = 0, curr_sum: int = 0) -> bool:
            if curr_sum == target:
                return True
            if i >= n or curr_sum > target:
                return False
            return dp(i + 1, curr_sum + nums[i]) or dp(i + 1, curr_sum)
        
        return dp()
