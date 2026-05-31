class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carMap = {}

        for index, pos in enumerate(position):
            carMap[pos] = speed[index]
        
        fleetStack = []
        position.sort()

        for i in reversed(position):
            timeToReach = (target - i) / carMap[i]
            
            if not fleetStack:
                fleetStack.append(timeToReach)

            if fleetStack[-1] < timeToReach:
                fleetStack.append(timeToReach)

        return len(fleetStack)
        





        

        