class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotations = {
            0 : 0,
            1 : 1,
            6 : 9,
            8 : 8,
            9 : 6
        }

        invalids = [2,3,4,5,7]
        rotatedNum = str(n)
        print(rotatedNum)

        power = 0
        flipped = 0

        for digit in rotatedNum:
            if int(digit) in invalids:
                return False
            else:
                flipped += rotations[int(digit)] * (10 ** power)
            power += 1
        
        print(flipped)

        return flipped != n

