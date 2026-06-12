class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
            valToPos = {}
            output = []

            for i in range(len(nums2)):
                valToPos[nums2[i]] = i
            
            for num in nums1:
                output.append(valToPos[num])
            
            return output