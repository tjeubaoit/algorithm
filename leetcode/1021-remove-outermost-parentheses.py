class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        outers = set()
        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if len(stack) == 1:
                    outers.add(stack[-1])
                    outers.add(i)
                stack.pop()
        ans = []
        for i, ch in enumerate(s):
            if i not in outers:
                ans.append(ch)
        return ''.join(ans)


if __name__ == '__main__':
    # s = '(()())(())'
    # s = '(()())(())(()(()))'
    s = '()()'
    ret = Solution().removeOuterParentheses(s)
    print(ret)
