from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.solution2(nums)

    def solution1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1]*n, [1]*n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        # print(left, right)

        ans = [0]*n
        for i in range(n):
            ans[i] = left[i] * right[i]
        return ans

    # O(1) space solution
    def solution2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        for i in range(n-2, -1, -1):
            ans[i] = ans[i+1] * nums[i+1]
        left = 1
        for i in range(n):
            ans[i] *= left
            left *= nums[i]
        return ans

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    ret = Solution().productExceptSelf(nums)
    print(ret)
