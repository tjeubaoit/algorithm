from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for n in pushed:
            stack.append(n)
            if n == popped[i]:
                # Only work if pushed and popped contain distinct values
                while stack and stack[-1] == popped[i]:
                    stack.pop()
                    i += 1
        return not stack


if __name__ == '__main__':
    # pushed = [1, 2, 3, 4, 5]
    # popped = [4, 5, 3, 2, 1]
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    ret = Solution().validateStackSequences(pushed, popped)
    print(ret)
