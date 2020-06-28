from typing import List


class Solution:

    # O(N) Time | O(N) space
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        ans = [0] * len(temps)
        stack = []
        for i, t in enumerate(temps):
            while stack and temps[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans

    # O(N) Time | O(W) space (W is the number of allowed values for T[i])
    def dailyTemperatures2(self, T):
        ans = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans


if __name__ == '__main__':
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    ret = Solution().dailyTemperatures(temps)
    print(ret)
