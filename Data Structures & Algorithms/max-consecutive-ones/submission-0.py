class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #nums is binary array - only contains 0s and 1s
        #I need to find the maximum subsequence of repeating 1s

        #I could use a for loop and then at each 1, I could do a nested loop to see how many 1s are after it, but this would be O(n^2) - imagine I have [1, 1, 1, 1, ...., 1] - an array of all 1s - this would not be very efficent in runtime
        #A better solution would be to use a 2 pointer kinda sliding window approach where I count forward every time I find a 1 and I just keep moving along it, now I have an O(n) approach as it doesn't repeat

        #clarifying questions: only 1s and 0s? only INT values? Will the list have at least 1 element? For an empty list, I'd return 0?

        maxSubOnes = 0
        i = 0

        count = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            i += 1
            maxSubOnes = max(maxSubOnes, count)
        
        return maxSubOnes