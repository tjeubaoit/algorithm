from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        while lo < hi:
            m = lo + (hi-lo)//2
            if nums[m] > nums[m+1]:
                hi = m
            elif nums[m] < nums[m+1]:
                lo = m+1
        return lo


if __name__ == '__main__':
    # nums = [1,2,1,3,5,6,4]
    # nums = [1,2,3,1]
    nums = [3,4,3,2,1]
    ret = Solution().findPeakElement(nums)
    print(ret)
