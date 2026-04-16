class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        while l < r:
            if nums[l] <= nums[m] <= nums[r] or nums[l] > nums[m]:
                r = m
            else:
                l = m + 1
            m = (l + r) // 2
        
        return nums[m]
        