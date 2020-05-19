class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        # If s and t is unicode string, use hash table instead
        counter = [0] * 26
        for i, ch in enumerate(s):
            counter[ord(ch)-ord('a')] += 1
            counter[ord(t[i])-ord('a')] -= 1
        for ct in counter:
            if ct != 0: return False
        return True


if __name__ == '__main__':
    ret = Solution().isAnagram('anagram', 'nagaram')
    print(ret)
