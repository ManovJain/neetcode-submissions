class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        outputTemps = [0] * len(temperatures)
        stack = [] #pair of value and index

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackIndex, stackTemp = stack.pop()
                outputTemps[stackIndex] = index - stackIndex
            stack.append([index, temp])

        print(outputTemps)

        return outputTemps

        
