class Solution:
    # noinspection PyTypeChecker
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        nums = [None] * len(num1)
        i, r, diff = len(num1) - 1, 0, len(num1) - len(num2)

        while i >= 0:
            x2 = int(num2[i-diff]) if i >= diff else 0
            s = int(num1[i]) + x2 + r
            nums[i], r = str(s % 10), s // 10
            i -= 1

        ans = ''.join(nums)
        return '1' + ans if r > 0 else ans


if __name__ == '__main__':
    ret = Solution().addStrings('1234', '9999')
    print(ret)
