from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        st = []
        l, r = len(nums), 0
        for i, n in enumerate(nums):
            while st and n < nums[st[-1]]:
                l = min(l, st.pop())
            st.append(i)
        st = []
        for i, n in enumerate(reversed(nums)):
            while st and n > nums[st[-1]]:
                r = max(r, st.pop())
            st.append(len(nums)-i-1)
        return r - l + 1 if r > l else 0


if __name__ == '__main__':
    # nums = [2, 6, 4, 8, 10, 9, 15]
    # nums = [2, 3, 3, 2, 4]
    # nums = [1, 3, 2, 2, 2]
    nums = [1, 3, 5, 4, 2]
    # nums = [1, 2, 4, 5, 3]
    ret = Solution().findUnsortedSubarray(nums)
    print(ret)
