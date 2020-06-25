from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = False
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                if flag:
                    return False
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                else:
                    nums[i+1] = nums[i]
                flag = True
        return True


if __name__ == '__main__':
    nums = [3, 4, 2, 3]
    # nums = [4, 2, 3]
    ret = Solution().checkPossibility(nums)
    print(ret)
