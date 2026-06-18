class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        nums1 = nums.copy()
        nums1.pop()

        for i in range(3, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i-1])
            nums[i-1] = max(nums[i-1], nums[i-2])
        
        for i in range(2, len(nums1)):
            nums1[i] = max(nums1[i] + nums1[i - 2], nums1[i-1])
            nums1[i-1] = max(nums1[i-1], nums1[i-2])
        
        return max(nums[-1], nums1[-1])

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) < 3:
#             return max(nums)
        
#         for i in range(2, len(nums)):
#             nums[i] = max(nums[i] + nums[i-2], nums[i-1])
#             nums[i-1] = max(nums[i-1], nums[i-2])
        
#         return nums[-1]