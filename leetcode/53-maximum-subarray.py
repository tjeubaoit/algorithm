from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum = 0, -2147483648
        for i in range(0, len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            curr_sum = max(curr_sum, 0)
        return max_sum

    def kadaneSolution(self, nums):
        max_so_far = max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
