from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        larger = [0] * n
        smaller = [0] * n
        for i in range(n - 2, -1, -1):
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    larger[i] += 1
                else:
                    smaller[i] += 1
        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                if rating[i] > rating[j]:
                    ans += smaller[j]
                else:
                    ans += larger[j]
        return ans


if __name__ == '__main__':
    nums = [2, 5, 3, 4, 1]
    ret = Solution().numTeams(nums)
    print(ret)
