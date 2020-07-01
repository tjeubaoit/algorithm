from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = dict()
        stack = []
        for i, n in enumerate(nums2):
            while stack and stack[-1] < n:
                greater[stack.pop()] = n
            stack.append(n)

        ans = [-1]*len(nums1)
        for i, n in enumerate(nums1):
            ans[i] = greater.get(n, -1)
        return ans


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 2, 3, 4]
    # nums1 = [4, 1, 2]
    # nums2 = [1, 3, 4, 2]
    ret = Solution().nextGreaterElement(nums1, nums2)
    print(ret)
