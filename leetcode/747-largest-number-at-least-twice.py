from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        mx1, mx2 = 0, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[mx1]:
                mx2 = mx1
                mx1 = i
            elif nums[i] > nums[mx2]:
                mx2 = i
        return mx1 if nums[mx2]*2 <= nums[mx1] else -1