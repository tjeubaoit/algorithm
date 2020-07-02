from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        i, ans, prod = 0, 0, 1
        for j, n in enumerate(nums):
            prod *= n
            while i <= j and prod >= k:
                prod //= nums[i]
                i += 1
            ans += j - i + 1
        return ans


if __name__ == '__main__':
    ret = Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(ret)
