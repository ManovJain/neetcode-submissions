class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        maxSeq = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                inc, dec = 1, 1
            elif nums[i] > nums[i-1]:
                inc = inc + 1
                dec = 1
            else:
                dec = dec + 1
                inc = 1
            
            maxSeq = max(inc, dec, maxSeq)
        
        return maxSeq
