from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.solution1(nums)

    # Hash map approach
    def solution1(self, nums: List[int]) -> int:
        ct = Counter()
        m = len(nums) // 2
        for n in nums:
            ct[n] += 1
            if ct[n] > m:
                return n

    # Divide and conquer approach
    def solution2(self, nums: List[int]) -> int:
        pass

    # Boyer-Moore Voting Algorithm
    def solution3(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)

        return candidate


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))
