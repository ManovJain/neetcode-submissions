class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        print("\nDP Array Evolution\n")
        print(f"i=0 -> {dp}")
        print(f"i=1 -> {dp}")

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            print(f"i={i} -> {dp}")

        print(f"\nFinal Answer: {dp[-1]}")
        return dp[-1]


