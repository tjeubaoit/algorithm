from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ct = [0] * 1001
        for n in arr1:
            ct[n] += 1
        idx = 0
        for n in arr2:
            while ct[n] > 0:
                arr1[idx] = n
                idx += 1
                ct[n] -= 1
        for i, c in enumerate(ct):
            while c > 0:
                arr1[idx] = i
                idx += 1
                c -= 1
        return arr1


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    ret = Solution().relativeSortArray(arr1, arr2)
    print(ret)
