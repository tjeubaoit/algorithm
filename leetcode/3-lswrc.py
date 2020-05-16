class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = dict()
        ret = 1 if s else 0
        slow, fast = 0, 0
        for fast, ch in enumerate(s):
            if index.get(ch, -1) >= slow:
                slow = index[ch] + 1
            else:
                ret = max(ret, fast - slow + 1)
            index[ch] = fast
        return ret


def test(expected, s):
    ret = Solution().lengthOfLongestSubstring(s)
    if ret != expected:
        raise ValueError({'input': s, 'expected': expected, 'output': ret})


if __name__ == '__main__':
    test(5, "tmmzuxt")
    test(3, 'abcabcbb')
    test(3, 'dvdf')
    test(3, 'pwwkew')
    test(1, 'bbbbbb')
