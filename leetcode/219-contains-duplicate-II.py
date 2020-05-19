from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i, n in enumerate(nums):
            if i != d[n] and i - d[n] <= k:
                return True
            d[n] = i
        return False


if __name__ == '__main__':
    ret = Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print(ret)
