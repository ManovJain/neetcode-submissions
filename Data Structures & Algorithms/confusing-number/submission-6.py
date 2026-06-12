class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotations = {
            "0" : 0,
            "1" : 1,
            "6" : 9,
            "8" : 8,
            "9" : 6
        }

        nString = str(n)
        power = 0
        flippedNum = 0

        for digit in nString:
            if digit not in rotations:
                return False

            flippedNum += rotations[digit] * ( 10 ** power )
            power += 1
        
        return flippedNum != n