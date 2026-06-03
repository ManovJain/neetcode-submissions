class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numHash = {}
        # self.maxSequence = 0

        # for i in nums:
        #     if i not in numHash:
        #         numHash[i] = 0
                
        # def calculateSubsequence():
        #     for i in numHash:
        #         if i - 1 not in numHash:
        #             count = 0
        #             while i in numHash:
        #                 count += 1
        #                 i += 1
        #             self.maxSequence = max(self.maxSequence, count)
        
        # calculateSubsequence()

        # return self.maxSequence


        numMap = {}
        maxSequence = 0

        for i in nums:
            if i not in numMap:
                numMap[i] = 0
        
        for i in numMap:
            if i - 1 not in numMap:
                count = 0
                while i in numMap:
                    count += 1
                    i += 1
                maxSequence = max(maxSequence, count)
        
        return maxSequence
