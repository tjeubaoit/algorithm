import math
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > math.log(n, 2):
            nums = sorted(nums, reverse=True)
            return nums[k - 1]

        min_val = min(nums)
        largs = [min_val]*k
        for i, v in enumerate(nums):
            j = 0
            while j < k and v <= largs[j]:
                j += 1
            t = v
            while j < k:
                largs[j], t = t, largs[j]
                j += 1
        return largs[-1]


if __name__ == '__main__':
    # nums = [3, 2, 1, 5, 6, 4]
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    ret = Solution().findKthLargest(nums, 4)
    print(ret)
