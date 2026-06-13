class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        r2lSum = 0

        for i in range(1, len(nums)):
            r2lSum += nums[i - 1]
            prefix.append(r2lSum)
        
        print(prefix)

        suffix = [0] * len(nums)
        n = len(nums) - 2
        l2rSum = 0
        while n > -1:
            l2rSum += nums[n + 1]
            suffix[n] = l2rSum
            n -= 1
        
        print(suffix)

        for i in range(len(prefix)):
            if prefix[i] == suffix[i]:
                return i
        
        return -1
        
