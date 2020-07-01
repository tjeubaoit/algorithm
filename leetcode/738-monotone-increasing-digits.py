class Solution:
    
    def toDigits(self, n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        return digits

    def toNumber(self, digits):
        n = 0
        for d in reversed(digits):
            n = n*10 + d
        return n

    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = self.toDigits(n)
        k = -1
        for i in range(len(digits)-1):
            if digits[i] < digits[i+1]:
                digits[i+1] -= 1
                k = i+1
        for i in range(k):
            digits[i] = 9
        return self.toNumber(digits)


if __name__ == '__main__':
    n = 332
    ret = Solution().monotoneIncreasingDigits(n)
    print(ret)
