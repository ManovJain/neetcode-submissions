class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        rollingSum = maxSum = nums[0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                rollingSum += nums[i]
            else:
                rollingSum = nums[i]
            
            maxSum = max(maxSum, rollingSum)
        
        return maxSum
        