class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        s = s.lower()
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        return True


if __name__ == '__main__':
    ret = Solution().isPalindrome('A man, a plan, a canal: Panama')
    print(ret)
