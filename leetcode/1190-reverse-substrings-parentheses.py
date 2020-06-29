class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, pos = [], [-1]*len(s)
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                l = stack.pop() + 1
                r = i - 1
                while l < r:
                    pos[r], pos[l] = pos[l], pos[r]
                    l += 1
                    r -= 1
            else:
                pos[i] = i
        ans = ''
        for i in pos:
            if i >= 0:
                ans += s[i]
        return ans


if __name__ == '__main__':
    # s = '(ed(et(oc))el)'
    # s = '(u(love)i)'
    s = 'a(bcdefghijkl(mno)p)q'
    ret = Solution().reverseParentheses(s)
    print(ret)
