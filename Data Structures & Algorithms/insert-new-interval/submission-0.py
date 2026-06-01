class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        returnArr = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                returnArr.append(newInterval)
                return returnArr + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                returnArr.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            
        returnArr.append(newInterval)
        return returnArr