from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return self.solution2(nums)

    def solution2(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans

    def solution1(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                j = nums[i] - 1
                while nums[j] != 0:
                    t = nums[j] - 1
                    nums[j] = 0
                    j = t
            i += 1
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(i+1)
        return ans


if __name__ == '__main__':
    ret = Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(ret)
