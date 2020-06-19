from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            m = lo + (hi - lo) // 2
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            if m % 2 == 0:
                if nums[m] == nums[m + 1]:
                    lo = m + 2
                else:
                    hi = m - 2
            else:
                if nums[m] == nums[m - 1]:
                    lo = m + 1
                else:
                    hi = m - 1
        return nums[lo]
