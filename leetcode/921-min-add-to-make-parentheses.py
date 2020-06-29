class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closed, opened = 0, 0
        for ch in s:
            if ch == '(':
                closed += 1
            elif closed > 0:
                closed -= 1
            else:
                opened += 1
        return opened + closed


if __name__ == '__main__':
    s = '())'
    # s = '((('
    # s = '()'
    # s = '()))(('
    ret = Solution().minAddToMakeValid(s)
    print(ret)
