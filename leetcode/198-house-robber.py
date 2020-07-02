from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    # O(1) space
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        elif n == 1: return nums[0]
        
        prev, curr = nums[0], max(nums[0], nums[1])
        for n in nums[2:]:
            prev, curr = curr, max(prev + n, curr)
        return curr
