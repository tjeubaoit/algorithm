from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i, v in enumerate(nums):
            index = abs(v) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            # If element appear twice
            elif nums[index] < 0:
                ans.append(index + 1)
        return ans


if __name__ == '__main__':
    nums = [5, 4, 6, 7, 9, 3, 10, 9, 5, 6]
    ret = Solution().findDuplicates(nums)
    print(ret)
