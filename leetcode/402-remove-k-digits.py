class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remove = set()
        for i, d in enumerate(num):
            while k > 0 and stack and num[stack[-1]] > d:
                remove.add(stack.pop())
                k -= 1
            stack.append(i)
        ans = ''
        for i, d in enumerate(num):
            if i+k == len(num):
                break
            if not ans and d == '0':
                continue
            if i not in remove:
                ans += d
        return ans or '0'


if __name__ == '__main__':
    # num, k = '1432219', 3
    num, k = '10200', 1
    ret = Solution().removeKdigits(num, k)
    print(ret)
