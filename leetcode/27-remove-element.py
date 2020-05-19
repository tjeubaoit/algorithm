from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def removeElement2(self, nums: List[int], val: int) -> int:
        """
        when elements to remove are rare
        """
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n
