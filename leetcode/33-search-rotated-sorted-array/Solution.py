class Solution:
    def search(self, nums, target):
        if not nums: return -1
        x, y = 0, len(nums) - 1
        while x <= y:
            m = x + (y - x) // 2
            if nums[m] > nums[0]:
                x = m + 1
            elif nums[m] < nums[0]:
                y = m
            else:
                x = y if nums[x] > nums[y] else y + 1
                break
        print(x, y)

        if target > nums[0]:
            lo, hi = 0, x - 1
        elif target < nums[0]:
            lo, hi = x, len(nums) - 1
        else:
            return 0
        print(lo, hi)

        while lo <= hi:
            m = lo + (hi - lo) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                hi = m - 1
            else:
                lo = m + 1
        return -1


if __name__ == '__main__':
    ret1 = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=2)
    ret2 = Solution().search(nums=[1], target=1)
    ret3 = Solution().search(nums=[1, 3], target=1)
    ret4 = Solution().search(nums=[1, 3], target=3)
    ret5 = Solution().search(nums=[3, 1], target=1)
    print(ret1, ret2, ret3, ret4, ret5)

    ret = Solution().search(nums=[1, 3, 5], target=5)
    print(ret)
