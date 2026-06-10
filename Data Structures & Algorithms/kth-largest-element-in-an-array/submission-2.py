class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        
        heapq.heapify(nums)

        kthNum = 0
        while k != 0:
            kthNum = heapq.heappop(nums)
            k -= 1
        
        return kthNum * -1
