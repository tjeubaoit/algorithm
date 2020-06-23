class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def findPower(x, cache):
            if x == 1:
                return 0
            elif x in cache:
                return cache[x]

            x2 = 3 * x + 1 if x % 2 != 0 else x // 2
            cache[x] = 1 + findPower(x2, cache)
            return cache[x]

        cache = {1: 0}
        for x in range(lo, hi + 1):
            if x not in cache:
                findPower(x, cache)

        nums = [n for n in range(lo, hi + 1)]
        nums = sorted(nums, key=lambda x: (cache[x], x))
        return nums[k - 1]
