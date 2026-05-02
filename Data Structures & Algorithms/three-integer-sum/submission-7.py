class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                s = nums[j] + nums[k]
                if s == -num:
                    res.append([num, nums[j], nums[k]])
                    k -= 1
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif s > -num:
                    k -= 1
                else:
                    j += 1
        
        return res
        