class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2 + 1):
            if s[i] == s[0] and len(s) % i == 0:
                j = i
                while j < len(s):
                    if s[j-i:j] != s[j:j+i]:
                        break
                    j += i
                if j == len(s):
                    return True
        return False


if __name__ == '__main__':
    s = "abab"
    ret = Solution().repeatedSubstringPattern(s)
    print(ret)
