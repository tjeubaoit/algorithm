class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        ct = 0
        for ch in s:
            if ch == '(':
                ct += 1
                if ct != 1:
                    ans.append(ch)
            else:
                ct -= 1
                if ct != 0:
                    ans.append(ch)
        return ''.join(ans)


if __name__ == '__main__':
    # s = '(()())(())'
    # s = '(()())(())(()(()))'
    s = '()()'
    ret = Solution().removeOuterParentheses(s)
    print(ret)
