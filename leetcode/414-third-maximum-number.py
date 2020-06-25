from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        t = min(nums)
        x1, x2, x3 = t, t, t
        for i in range(0, len(nums)):
            if nums[i] > x1:
                x3 = x2
                x2 = x1
                x1 = nums[i]
            elif x1 > nums[i] > x2:
                x3 = x2
                x2 = nums[i]
            elif x2 > nums[i] > x3:
                x3 = nums[i]
        return x3 if x3 < x2 < x1 else x1


if __name__ == '__main__':
    nums = [2, 2, 3, 1]
    ret = Solution().thirdMax(nums)
    print(ret)
