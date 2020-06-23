from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        limits = [2, 9, 5, 9]
        nums = sorted(A, reverse=True)

        def backtrack(ans, i):
            for j in range(4):
                t = nums[j]
                # Get valid range for current index
                lm = 3 if i == 1 and ans[0] == 2 else limits[i]

                if 0 <= nums[j] <= lm:
                    ans[i] = nums[j]
                    # Mark value at current index as unavailable
                    nums[j] = -1
                    if i == 3:
                        return '%s%s:%s%s' % tuple(ans)
                    else:
                        ret = backtrack(ans, i+1)
                        if ret:  # If found answer then return
                            return ret
                # Revert value at current index as available
                nums[j] = t
            return ''

        ans = [-1] * 4
        return backtrack(ans, 0)


if __name__ == '__main__':
    A = [2, 0, 6, 6]
    ret = Solution().largestTimeFromDigits(A)
    print(ret)
