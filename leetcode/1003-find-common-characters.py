from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cts = [[0] * 26 for _ in range(len(A))]
        for i, s in enumerate(A):
            for ch in s:
                cts[i][ord(ch) - ord('a')] += 1

        ans = []
        for idx in range(26):
            c = 100
            for i in range(len(A)):
                c = min(c, cts[i][idx])
            ch = chr(idx + ord('a'))
            while c > 0:
                ans.append(ch)
                c -= 1
        return ans


if __name__ == '__main__':
    strs = ["bella", "label", "roller"]
    ret = Solution().commonChars(strs)
    print(ret)
