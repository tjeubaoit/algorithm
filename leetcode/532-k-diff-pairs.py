class Solution:
    def findPairs(self, nums, k: int) -> int:
        if k < 0: return 0
        seen = dict()
        for i, n in enumerate(nums):
            seen[n + k] = i
        ans = 0
        for i, n in enumerate(nums):
            if seen.get(n, -1) >= 0 and seen[n] != i:
                ans += 1
                seen[n] = -1
        return ans


if __name__ == '__main__':
    ret = Solution().findPairs([3, 1, 4, 1, 5], 2)
    print(ret)
