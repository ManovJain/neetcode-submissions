class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        localMaxHeap = []
        localMaxes = []

        for i in range(len(nums)):
            heapq.heappush(localMaxHeap, (-nums[i], i))
            if i >= k - 1:
                while localMaxHeap[0][1] <= i - k:
                    heapq.heappop(localMaxHeap)
                localMaxes.append(-localMaxHeap[0][0])
        
        return localMaxes
                
