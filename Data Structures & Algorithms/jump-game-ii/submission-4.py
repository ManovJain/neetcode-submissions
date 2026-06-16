class Solution:
    def jump(self, nums: List[int]) -> int:
        left = right = 0

        level = 0
        while right < len(nums) - 1:
            bigJump = 0
            for i in range(left, right + 1):
                bigJump = max(i + nums[i], bigJump)
            left = right + 1
            right = bigJump
            level += 1

        return level