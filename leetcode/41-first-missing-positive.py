from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, v in enumerate(nums):
            # We don't care about non-positive numbers
            # so we mark it as positive and larger than n.
            # These numbers will be ignored in the next steps
            if v <= 0:
                nums[i] = abs(v) + n + 1
        for i, v in enumerate(nums):
            index = abs(v) - 1
            # Ignore numbers with index larger than n
            if index < n and nums[index] > 0:
                nums[index] = -nums[index]
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n + 1


if __name__ == '__main__':
    # nums = [7, 8, 9, 11, 12]
    # nums = [3, 4, -1, 1]
    nums = [0, 1, 2]
    ret = Solution().firstMissingPositive(nums)
    print(ret)
