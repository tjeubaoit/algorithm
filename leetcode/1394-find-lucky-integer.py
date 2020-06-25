import math
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return self.solution1(arr)

    def solution1(self, arr: List[int]) -> int:
        ct = [0]*501
        for n in arr:
            ct[n] += 1
        for i in range(500, 0, -1):
            if ct[i] == i:
                return i
        return -1

    def solution2(self, arr: List[int]) -> int:
        # Did not work
        n = len(arr)
        for i, v in enumerate(arr):
            if v > n: continue
            index = (abs(v) - 1) % n
            if arr[index] > 0:
                arr[index] = -arr[index]
            else:
                arr[index] -= n
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] < 0 and math.ceil(abs(arr[i]) / n) == i + 1:
                return i + 1
        return -1


if __name__ == '__main__':
    tests = [
        ([2, 2, 3, 4], 2),
        ([1, 2, 2, 3, 3, 3], 3),
        ([2, 2, 2, 3, 3], -1),
        ([7, 7, 7, 7, 7, 7, 7], 7),
        ([13, 16, 7, 3, 14, 4, 12, 19, 6, 6, 7, 16, 17, 17], -1)
    ]
    for nums, expected in tests:
        ret = Solution().findLucky(nums)
        if ret != expected:
            print(nums, ret)
            break
