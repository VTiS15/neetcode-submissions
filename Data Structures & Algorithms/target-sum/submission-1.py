class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(nums: Tuple[int, ...], target: int) -> bool:
            if len(nums) == 1:
                return int(nums[0] == target)
            return dp((nums[0] + nums[1],) + nums[2:], target) + dp((nums[0] - nums[1],) + nums[2:], target)
        
        return dp((0,) + tuple(nums), target)
        