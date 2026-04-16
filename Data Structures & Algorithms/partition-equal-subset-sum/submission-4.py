from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        # If sum of nums is odd we can immediately return False
        if s % 2 != 0:
            return False

        n = len(nums)
        target = s // 2
        
        # Dynamic programming function
        @cache
        def dp(i: int = 0, curr_sum: int = 0) -> bool:
            # Base case 1: Return True if curr_sum equals target
            if curr_sum == target:
                return True
            # Base case 2: Return False if curr_sum still does not equal target after processing all numbers in nums or curr_sum is greater than target
            if i >= n or curr_sum > target:
                return False
            # Recursive case: Either include the ith number or not and continue
            return dp(i + 1, curr_sum + nums[i]) or dp(i + 1, curr_sum)
        
        return dp()
