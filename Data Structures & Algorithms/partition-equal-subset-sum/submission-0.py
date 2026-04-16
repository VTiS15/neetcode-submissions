class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)

        if s % 2 != 0:
            return False

        target = s // 2
        
        def dp(i: int = 0, curr_sum: int = 0) -> bool:
            if i >= n or curr_sum > target:
                return False
            if curr_sum == target:
                return True
            return dp(i + 1, curr_sum + nums[i]) or dp(i + 1, curr_sum)
        
        return dp()
