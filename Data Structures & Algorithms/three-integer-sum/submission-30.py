class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        combos = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = val + nums[left] + nums[right]
                if sum == 0:
                    combos.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return combos
