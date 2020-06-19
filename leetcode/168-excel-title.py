class Solution:
    def convertToTitle(self, n: int) -> str:
        return self.solution1(n)

    def solution1(self, n: int) -> str:
        ans = []
        while n > 0:
            n, r = divmod(n-1, 26)
            ans.append(chr(r + ord('A')))
        return ''.join(ans[::-1])

    # time limit exceeded
    def solution2(self, n: int) -> str:
        if n == 0: return ''
        p = (n-1) // 26
        ans = []
        for _ in range(p):
            if not ans:
                ans.append('A')
            else:
                i = len(ans)-1
                while ans[i] == 'Z':
                    ans[i] = 'A'
                    i -= 1
                if i < 0:
                    ans.append('A')
                else:
                    ans[i] = chr(ord(ans[i]) + 1)
        if n > p * 26:
            ans.append(chr(ord('A') + n - p * 26 - 1))
        return ''.join(ans)


if __name__ == '__main__':
    for n in range(52, 80):
        ret = Solution().convertToTitle(n)
        print(n, ret)
