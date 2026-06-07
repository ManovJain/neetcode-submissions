class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = []
        for p in range(len(position)):
            time = [position[p], speed[p]]
            times.append(time)
        
        times.sort(reverse = True)

        for index in range(len(times)):
            times[index] = (target - times[index][0]) / times[index][1] 
        
        print(times)

        stack = []

        for time in times:
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)


        