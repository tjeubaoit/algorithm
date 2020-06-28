from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums)
        for i in range(2*len(nums)):
            idx = i % len(nums)
            while stack and nums[stack[-1]] < nums[idx]:
                ans[stack.pop()] = nums[idx]
            if ans[idx] < 0:
                stack.append(idx)
        return ans


if __name__ == '__main__':
    temps = [1, 2, 1]
    ret = Solution().nextGreaterElements(temps)
    print(ret)
