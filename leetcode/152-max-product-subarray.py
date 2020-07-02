from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        imax, imin = 1, 1
        ans = nums[0]
        for n in nums:
            if n > 0:
                imax, imin = max(imax*n, n), min(imin*n, n)
            else:
                imax, imin = max(imin*n, n), min(imax*n, n)
            ans = max(ans, imax)
        return ans


if __name__ == '__main__':
    # nums = [-2, 0, -1]
    # nums = [2, 3, -2, 4]
    # nums = [-2,3,-4]
    nums = [-4,-3,-2]
    ret = Solution().maxProduct(nums)
    print(ret)
