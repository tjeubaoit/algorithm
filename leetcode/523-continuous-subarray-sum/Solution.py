from collections import Counter

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = [0]*(len(nums)+1)
        d = {0: 0}
        for i in range(0, len(nums)):
            sums[i+1] = sums[i] + nums[i]
            mod = sums[i+1] % k if k != 0 else sums[i+1]
            if mod in d:
                if i + 1 - d[mod] >= 2: return True
            else:
                d[mod] = i + 1
        return False
    