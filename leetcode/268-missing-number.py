from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.sumSolution(nums)

    def haflSumSolution(self, nums):
        n = len(nums)
        m = n // 2
        s = 0 if n % 2 != 0 else m
        for num in nums:
            if num <= m:
                s += num - n
            else:
                s += num
        return -s if s < 0 else n - s

    def sumSolution(self, nums):
        ret = 0
        for i, num in enumerate(nums):
            ret += (i + 1) - nums[i]
        return ret

    def bitSolution(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    # sum = n*(n+1)/2
    def gaussSolution(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
