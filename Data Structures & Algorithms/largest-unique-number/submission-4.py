class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        occurances = defaultdict(int)

        for num in nums:
            occurances[num] += 1
        
        nums.sort(reverse=True)
        for num in nums:
            if occurances[num] == 1:
                return num
        
        return -1
