from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j, n = 0, 0, len(nums)
        ans, product = 0, 1
        while i <= j:
            while product < k or j < n - 1:
                product *= nums[j]
                ans += 1
                j += 1
            product //= nums[i]
            i += 1
        return ans


if __name__ == '__main__':
    ret = Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(ret)
