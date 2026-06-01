class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = mid = 0
        high = len(nums) - 1

        def swap(num1, num2):
            temp = nums[num1]
            nums[num1] = nums[num2]
            nums[num2] = temp 

        while mid <= high:
            if nums[mid] == 2:
                swap(mid, high)
                high -= 1
            elif nums[mid] == 0:
                swap(mid, low)
                low += 1
                mid += 1
            else:
                mid += 1
            
        return nums