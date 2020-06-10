from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = dict()
        ans = 0
        sums = [0]*(len(nums)+1)
        for i in range(1, len(sums)):
            n = -1 if nums[i-1] == 0 else 1
            sums[i] = sums[i-1] + n
            if sums[i] == 0:
                ans = max(ans, i)
            elif sums[i] in d:
                ans = max(ans, i - d[sums[i]])
            else:
                d[sums[i]] = i
        return ans


if __name__ == '__main__':
    nums = [0, 1]
    ret = Solution().findMaxLength(nums)
    print(ret)
